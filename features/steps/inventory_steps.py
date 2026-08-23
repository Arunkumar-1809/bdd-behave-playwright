from behave import given, when, then

PRODUCT_ID_MAP = {
    "Sauce Labs Backpack": "sauce-labs-backpack",
    "Sauce Labs Bike Light": "sauce-labs-bike-light",
    "Sauce Labs Bolt T-Shirt": "sauce-labs-bolt-t-shirt",
    "Sauce Labs Fleece Jacket": "sauce-labs-fleece-jacket",
    "Sauce Labs Onesie": "sauce-labs-onesie",
    "Test.allTheThings() T-Shirt (Red)": "test.allthethings()-t-shirt-(red)",
}


def _add_to_cart_button_id(product_name):
    slug = PRODUCT_ID_MAP.get(product_name)
    if not slug:
        raise ValueError(f"Unknown product name: {product_name}")
    return f"add-to-cart-{slug}"


def _remove_button_id(product_name):
    slug = PRODUCT_ID_MAP.get(product_name)
    if not slug:
        raise ValueError(f"Unknown product name: {product_name}")
    return f"remove-{slug}"


@when('I add "{product_name}" to the cart')
def step_add_product_to_cart(context, product_name):
    button_id = _add_to_cart_button_id(product_name)
    context.page.click(f'[data-test="{button_id}"]')


@given('I have added "{product_name}" to the cart')
def step_given_added_to_cart(context, product_name):
    step_add_product_to_cart(context, product_name)


@when('I remove "{product_name}" from the cart')
def step_remove_product_from_cart(context, product_name):
    button_id = _remove_button_id(product_name)
    context.page.click(f'[data-test="{button_id}"]')


@then('the cart badge should show "{count}"')
def step_cart_badge_shows(context, count):
    badge_text = context.page.inner_text(".shopping_cart_badge")
    assert badge_text == count, f"Expected cart badge '{count}', got '{badge_text}'"


@then('the cart badge should not be visible')
def step_cart_badge_not_visible(context):
    badge_count = context.page.locator(".shopping_cart_badge").count()
    assert badge_count == 0, "Expected cart badge to be absent, but it is visible"


@when('I sort products by "{sort_label}"')
def step_sort_products(context, sort_label):
    context.page.select_option(".product_sort_container", label=sort_label)


@then('the first product listed should be "{product_name}"')
def step_first_product_should_be(context, product_name):
    first_item_name = context.page.inner_text(".inventory_item_name >> nth=0")
    assert first_item_name == product_name, (
        f"Expected first product '{product_name}', got '{first_item_name}'"
    )
