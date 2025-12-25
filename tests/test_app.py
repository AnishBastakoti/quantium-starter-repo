from dashboard import app

def test_header_present(dash_duo):
    """
    Verify the page header is present.
    """
    dash_duo.start_server(app)

    header = dash_duo.find_element("h4")
    assert header is not None
    assert header.text == "Pink Morsels Sales"


def test_visualisation_present(dash_duo):
    """
    Verify the sales graph is present.
    """
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#example-graph")
    assert graph is not None


def test_region_picker_present(dash_duo):
    """
    Verify the region radio selector is present.
    """
    dash_duo.start_server(app)

    region_selector = dash_duo.find_element("#region-selector")
    assert region_selector is not None
