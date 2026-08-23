from behave import given, when, then, register_type
from parse import with_pattern


@with_pattern(r".*")
def parse_maybe_empty(text):
    return text


register_type(MaybeEmpty=parse_maybe_empty)


@given('I am on the Sauce Demo login page')
def step_on_login_page(context):
    context.page.goto(context.base_url)


@given('I am logged in as "{username}"')
def step_logged_in_as(context, username):
    context.page.goto(context.base_url)
    context.page.fill("#user-name", username)
    context.page.fill("#password", "secret_sauce")
    context.page.click("#login-button")
    context.page.wait_for_selector(".inventory_list")


@when('I log in with username "{username:MaybeEmpty}" and password "{password:MaybeEmpty}"')
def step_log_in(context, username, password):
    context.page.fill("#user-name", username)
    context.page.fill("#password", password)
    context.page.click("#login-button")


@then('I should be redirected to the inventory page')
def step_redirected_to_inventory(context):
    context.page.wait_for_url("**/inventory.html")
    assert "inventory.html" in context.page.url


@then('I should see the page title "{title}"')
def step_see_page_title(context, title):
    header_text = context.page.inner_text(".title")
    assert header_text == title, f"Expected title '{title}', got '{header_text}'"


@then('I should see an error message containing "{message}"')
def step_see_error_message(context, message):
    error_text = context.page.inner_text('[data-test="error"]')
    assert message in error_text, f"Expected error containing '{message}', got '{error_text}'"
