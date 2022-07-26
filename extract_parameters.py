#!/bin/env python3

import glob
from __future__ import print_function, division
from netCDF4 import Dataset
from wrf import (getvar, ALL_TIMES, extract_vars)
import xarray as xr
import numpy as np


%matplotlib inline

def write_xarray_to_netcdf(xarray_array, output_path,mode='w', format='NETCDF4', group=None, engine=None,
                           encoding=None):
    """writes and xarray in a netcdf format outputfile
    Uses the xarray typical for wrf-python. The projection objects are transformed into strings
    to be able to use them as netcdf attributes
    :param xarray_array: xarray.DataArray
    :param output_path: str
    :param format: 'NETCDF4', 'NETCDF4_CLASSIC', 'NETCDF3_64BIT' or 'NETCDF3_CLASSIC'
                    default: 'NETCDF4'
    :param group: str, default None
    :param engine: 'netcdf4', 'scipy' or 'h5netcdf'
    :param encoding: dict, default: None
    """
    xarray_array_out = xarray_array.copy(deep=True)
    # coordinates are extracted from variable
    del xarray_array_out.attrs['coordinates']
    # wrf-python projection object cannot be processed
    xarray_array_out.attrs['projection'] = str(xarray_array_out.attrs['projection'])

    xarray_array_out.to_netcdf(path=output_path, mode=mode, format=format, group=group,
                               engine=engine,
                               encoding=encoding)

# class InputFile():
#     ''' see how to do it '''
#     def __init__(self, 3dvars=None, 2dvars=None, levels='all'):
#         3dvars = self.3dvars
#         2dvars = self.2dvars
#         levels = self.all
# 
# def extract3Dvar(list_of_variables):
#     
