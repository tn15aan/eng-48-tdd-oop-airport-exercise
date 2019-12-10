from plane_class import *

def test_initializing_plane():
    # Setup
    plane1 = Plane('Boeing 737', 'BA4534')
    plane2 = Plane('Boeing 747', 'CP7543')
    # Assertion
    assert plane1.plane == 'Boeing 737'
    assert plane1.planeNumber == 'BA4534'
    assert plane2.plane == 'Boeing 747'
    assert plane2.planeNumber == 'CP7543'
