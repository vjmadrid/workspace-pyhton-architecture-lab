# -*- coding: utf-8 -*-


"""
Utilities
"""


from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from acme.selenium.extensions.condition_extension import Condition
from acme.selenium.utils.wait_util import wait_for
from common.utils.sleep_util import sleep


class WebElementEx(object):
    """
    WebElementEx is an extension of the selenium WebElement that fixes the clears method for the react elements. This
        code should be removed along with all references to .element in tests and the corresponding code in
        safe_find above.
        The bug is documented here:  https://github.com/SeleniumHQ/selenium/issues/6837
    """
    def __init__(self, name, page, scope, locator, web_element=None):
        self._scope = scope
        self._elements = locator.elements
        self._locator = locator
        self.name = name
        self.page = page
        self._web_element = web_element
        for key in self.keys:
            locator = self._elements[key]
            setattr(self, key, WebElementEx(key, page, self, locator))

    def __getattribute__(self, item):
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self.element.get_attribute(item) \
                or self.element.get_attribute(item.replace('_', '-')) \
                or self.element.__getattribute__(item)

    def __getitem__(self, item):
        return self.all[item]

    @property
    def scope(self):
        if isinstance(self._scope, WebElementEx):
            return self._scope.element
        else:
            return self._scope

    @property
    def locator(self):
        return self._locator.by, self._locator.value

    @property
    def element(self):
        if self._web_element is not None:
            try:
                return self._web_element
            except NoSuchElementException:
                self._web_element = None
                return self.element
        else:
            try:
                result = self._scope.find_element(*self.locator)
                self._web_element = result
                return result

            except TimeoutException:
                raise NoSuchElementException(msg=f'Unable to locate {self.name} on {self.page} using locator {self.locator}')

    @property
    def all(self):
        try:
            wait_for(self.is_present, timeout=0)
            result = self._scope.find_elements(*self.locator)
            return [WebElementEx(self.name, self.page, self._scope, self._locator, web_element=web_element) for web_element in result]

        except TimeoutException:
            raise NoSuchElementException(msg=f'Unable to locate {self.name} in {self._scope.name} using locator {self.locator}')

    @property
    def classes(self):
        return self.element.get_attribute('class').split(' ')

    @property
    def count(self):
        return len(self._scope.find_elements(*self.locator))

    def hover(self, wait=0):
        self.page.mouse.move_to_element(self.element).perform()
        sleep(wait)
        self.page.mouse.reset_actions()

    @property
    def keys(self):
        return list(self._elements.keys())

    @property
    def selenium_id(self):
        return self.element.id

    @property
    def is_present(self):
        return Condition(ec.presence_of_element_located(self.locator), self._scope)

    @property
    def is_stale(self):
        return Condition(ec.staleness_of(self.element), self._scope)

    @property
    def is_visible(self):
        return Condition(ec.visibility_of(self.element), self._scope)

    @property
    def is_invisible(self):
        return Condition(ec.invisibility_of_element(self.element), self._scope)

    @property
    def is_clickable(self):
        return Condition(ec.element_to_be_clickable(self.locator), self._scope)

    @property
    def is_selected(self):
        return Condition(ec.element_to_be_selected(self.element), self._scope)

    @property
    def is_not_selected(self):
        return Condition(ec.element_selection_state_to_be(self.element, False), self._scope)

    def has_text(self, text):
        return Condition(ec.text_to_be_present_in_element(self.locator, text), self._scope)

    def has_class(self, class_name):
        return Condition(lambda x: class_name in self.classes)

    def clear(self):
        self.element.send_keys(Keys.CONTROL, 'a')
        self.element.send_keys(Keys.DELETE)

    def test(self):
        try:
            with self._setup_test_context():
                assert self._locator.exclude or (bool(self.element) and self.count == self._locator.number)
                for key in self.keys:
                    getattr(self, key).test()
        except NoSuchElementException as e:
            assert False, e.msg

    # @contextmanager
    # def _setup_test_context(self):
    #    if self._locator.test_func is not None:
    #        with getattr(self.page, self._locator.test_func)():
    #            yield
    #    else:
    #        yield
