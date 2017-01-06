import os
import yaml
from nose.tools import assert_equal
from ..greengraph import Greengraph, Map
import numpy as np
from numpy import testing as npTest

# Test Greengraph initialisation
def test_Greengraph():
    mygraph=Greengraph('London', 'Cambridge')
    assert_equal(mygraph.start, 'London')
    assert_equal(mygraph.end, 'Cambridge')

# Test geolocate
def test_geolocate():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'places.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for item in fixtures:
            place  = item.pop('place')
            result = item.pop('result')
            mygraph=Greengraph('', '')
            data=list(mygraph.geolocate(place))
            assert_equal(result,data)

# Test location_sequence
def test_location_sequence():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'locations_sequence.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for item in fixtures:
            start = item.pop('start')
            stop = item.pop('stop')
            steps = item.pop('steps')
            result = item.pop('result')
            mygraph=Greengraph('', '')
            data = mygraph.location_sequence(start, stop, steps)
            npTest.assert_array_almost_equal(np.asarray(result), data)

# Test green_between
def test_green_between():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'greenbetween.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for item in fixtures:
            startLoc   = item.pop('start')
            startCoord = item.pop('startCoord')
            stopLoc     = item.pop('stop')
            stopCoord   = item.pop('stopCoord')
            steps     = item.pop('steps')
            result    = item.pop('result')
            mygraph=Greengraph(startLoc, stopLoc)
            data = mygraph.green_between(steps)
            assert_equal(result, data)

