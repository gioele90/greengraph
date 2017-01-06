import os
import yaml
from nose.tools import assert_equal
from ..greengraph import Map
import requests
from unittest.mock import patch, Mock
import numpy as np
from numpy import testing as npTest
from matplotlib import image as img

# Test Map initialisation with mocking (doesn't seem to work)
def test_Map():
	with patch.object(requests,'get') as mock_get:
		myMap=Map(51.0,0.0)
		mock_get.assert_called_with(
		"http://maps.googleapis.com/maps/api/staticmap?",
		params={
		'sensor':'false',
		'zoom':12,
		'size':'400x400',
		'center':'51.0,0.0',
		'style':'feature:all|element:labels|visibility:off'
		}
		)
            
# Test green function
def test_green():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'green.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for item in fixtures:
            coord = item.pop('coord')
            result = item.pop('result')
            myMap = Map(coord[0], coord[1], size=(5,5))
            data = myMap.green(1)
            npTest.assert_array_equal(np.asarray(result), data)

# Test count_green
def test_count_green():
    with open(os.path.join(os.path.dirname(__file__),'fixtures', 'green.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for item in fixtures:
            coord = item.pop('coord')
            count = item.pop('count')
            myMap = Map(coord[0], coord[1], size=(5,5))
            data = myMap.count_green(1)
            assert_equal(count, data)