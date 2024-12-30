"""
    pint_array
    ~~~~~~~~~~

    Pint interoperability with array API standard arrays.
"""

from __future__ import annotations

from typing import Generic

# from .quantity import ArrayUnitQuantity
from pint.facets.plain import MagnitudeT, PlainQuantity
from pint import Quantity

__all__ = ["pint_namespace", "ArrayUnitQuantity"]

import types


def pint_namespace(xp):

    mod = types.ModuleType(f'pint({xp.__name__})')

    class ArrayQuantity(Generic[MagnitudeT], PlainQuantity[MagnitudeT]):
        """ """
        def __init__(self, *args, xp, **kwargs):
            super().__init__()
            self._xp = xp

        # def __new__(self, *args, **kwargs):
        #     super().__new__(self, *args, **kwargs)

        def __array_namespace__(self):
            return mod

        # def _numpy_method_wrap(self, func, *args, **kwargs):
        #     """Convenience method to wrap on the fly NumPy ndarray methods taking
        #     care of the units.
        #     """

        #     # Set input units if needed
        #     if func.__name__ in set_units_ufuncs:
        #         self.__ito_if_needed(set_units_ufuncs[func.__name__][0])

        #     value = func(*args, **kwargs)

        #     # Set output units as needed
        #     if func.__name__ in (
        #         matching_input_copy_units_output_ufuncs
        #         + copy_units_output_ufuncs
        #         + self._wrapped_numpy_methods
        #     ):
        #         output_unit = self._units
        #     elif func.__name__ in set_units_ufuncs:
        #         output_unit = set_units_ufuncs[func.__name__][1]
        #     elif func.__name__ in matching_input_set_units_output_ufuncs:
        #         output_unit = matching_input_set_units_output_ufuncs[func.__name__]
        #     elif func.__name__ in op_units_output_ufuncs:
        #         output_unit = get_op_output_unit(
        #             op_units_output_ufuncs[func.__name__],
        #             self.units,
        #             list(args) + list(kwargs.values()),
        #             self._magnitude.size,
        #         )
        #     else:
        #         output_unit = None

        #     if output_unit is not None:
        #         return self.__class__(value, output_unit)

        #     return value

        # def __array__(self, t=None) -> np.ndarray:
        #     if HAS_NUMPY and isinstance(self._magnitude, np.ndarray):
        #         warnings.warn(
        #             "The unit of the quantity is stripped when downcasting to ndarray.",
        #             UnitStrippedWarning,
        #             stacklevel=2,
        #         )
        #     return _to_magnitude(self._magnitude, force_ndarray=True)

        # def clip(self, min=None, max=None, out=None, **kwargs):
        #     if min is not None:
        #         if isinstance(min, self.__class__):
        #             min = min.to(self).magnitude
        #         elif self.dimensionless:
        #             pass
        #         else:
        #             raise DimensionalityError("dimensionless", self._units)

        #     if max is not None:
        #         if isinstance(max, self.__class__):
        #             max = max.to(self).magnitude
        #         elif self.dimensionless:
        #             pass
        #         else:
        #             raise DimensionalityError("dimensionless", self._units)
        #     return self.__class__(self.magnitude.clip(min, max, out, **kwargs), self._units)

        # def fill(self: NumpyQuantity, value) -> None:
        #     self._units = value._units
        #     return self.magnitude.fill(value.magnitude)

        # def put(self: NumpyQuantity, indices, values, mode="raise") -> None:
        #     if isinstance(values, self.__class__):
        #         values = values.to(self).magnitude
        #     elif self.dimensionless:
        #         values = self.__class__(values, "").to(self)
        #     else:
        #         raise DimensionalityError("dimensionless", self._units)
        #     self.magnitude.put(indices, values, mode)

        # @property
        # def real(self) -> NumpyQuantity:
        #     return self.__class__(self._magnitude.real, self._units)

        # @property
        # def imag(self) -> NumpyQuantity:
        #     return self.__class__(self._magnitude.imag, self._units)

        # @property
        # def T(self):
        #     return self.__class__(self._magnitude.T, self._units)

        # @property
        # def flat(self):
        #     for v in self._magnitude.flat:
        #         yield self.__class__(v, self._units)

        # @property
        # def shape(self) -> Shape:
        #     return self._magnitude.shape

        # @property
        # def dtype(self):
        #     return self._magnitude.dtype

        # @shape.setter
        # def shape(self, value):
        #     self._magnitude.shape = value

        # def searchsorted(self, v, side="left", sorter=None):
        #     if isinstance(v, self.__class__):
        #         v = v.to(self).magnitude
        #     elif self.dimensionless:
        #         v = self.__class__(v, "").to(self)
        #     else:
        #         raise DimensionalityError("dimensionless", self._units)
        #     return self.magnitude.searchsorted(v, side)

        # def dot(self, b):
        #     """Dot product of two arrays.

        #     Wraps np.dot().
        #     """

        #     return np.dot(self, b)

        # @method_wraps("prod")
        # def prod(self, *args, **kwargs):
        #     """Return the product of quantity elements over a given axis

        #     Wraps np.prod().
        #     """
        #     return np.prod(self, *args, **kwargs)

        # def __ito_if_needed(self, to_units):
        #     if self.unitless and to_units == "radian":
        #         return

        #     self.ito(to_units)

        # def __len__(self) -> int:
        #     return len(self._magnitude)

        # def __getattr__(self, item) -> Any:
        #     if item.startswith("__array_"):
        #         # Handle array protocol attributes other than `__array__`
        #         raise AttributeError(f"Array protocol attribute {item} not available.")
        #     elif item in HANDLED_UFUNCS or item in self._wrapped_numpy_methods:
        #         magnitude_as_duck_array = _to_magnitude(
        #             self._magnitude, force_ndarray_like=True
        #         )
        #         try:
        #             attr = getattr(magnitude_as_duck_array, item)
        #             return functools.partial(self._numpy_method_wrap, attr)
        #         except AttributeError:
        #             raise AttributeError(
        #                 f"NumPy method {item} not available on {type(magnitude_as_duck_array)}"
        #             )
        #         except TypeError as exc:
        #             if "not callable" in str(exc):
        #                 raise AttributeError(
        #                     f"NumPy method {item} not callable on {type(magnitude_as_duck_array)}"
        #                 )
        #             else:
        #                 raise exc
        #     elif (
        #         HAS_UNCERTAINTIES and item == "ndim" and isinstance(self._magnitude, UFloat)
        #     ):
        #         # Dimensionality of a single UFloat is 0, like any other scalar
        #         return 0

        #     try:
        #         return getattr(self._magnitude, item)
        #     except AttributeError:
        #         raise AttributeError(
        #             "Neither Quantity object nor its magnitude ({}) "
        #             "has attribute '{}'".format(self._magnitude, item)
        #         )

        # def __getitem__(self, key):
        #     try:
        #         return type(self)(self._magnitude[key], self._units)
        #     except PintTypeError:
        #         raise
        #     except TypeError:
        #         raise TypeError(
        #             "Neither Quantity object nor its magnitude ({})"
        #             "supports indexing".format(self._magnitude)
        #         )

        # def __setitem__(self, key, value):
        #     try:
        #         # If we're dealing with a masked single value or a nan, set it
        #         if (
        #             isinstance(self._magnitude, np.ma.MaskedArray)
        #             and np.ma.is_masked(value)
        #             and getattr(value, "size", 0) == 1
        #         ) or (getattr(value, "ndim", 0) == 0 and math.isnan(value)):
        #             self._magnitude[key] = value
        #             return
        #     except TypeError:
        #         pass

        #     try:
        #         if isinstance(value, self.__class__):
        #             factor = self.__class__(
        #                 value.magnitude, value._units / self._units
        #             ).to_root_units()
        #         else:
        #             factor = self.__class__(value, self._units ** (-1)).to_root_units()

        #         if isinstance(factor, self.__class__):
        #             if not factor.dimensionless:
        #                 raise DimensionalityError(
        #                     value,
        #                     self.units,
        #                     extra_msg=". Assign a quantity with the same dimensionality "
        #                     "or access the magnitude directly as "
        #                     f"`obj.magnitude[{key}] = {value}`.",
        #                 )
        #             self._magnitude[key] = factor.magnitude
        #         else:
        #             self._magnitude[key] = factor

        #     except PintTypeError:
        #         raise
        #     except TypeError as exc:
        #         raise TypeError(
        #             f"Neither Quantity object nor its magnitude ({self._magnitude}) "
        #             "supports indexing"
        #         ) from exc


    class ArrayUnitQuantity(ArrayQuantity, Quantity):
        def __new__(cls, *args, xp, **kwargs):
            return super().__new__(cls, *args, **kwargs)

        def __init__(self, *args, xp, **kwargs):
            ArrayQuantity.__init__(self, *args, xp=xp, **kwargs)
            Quantity.__init__(self)
            self._xp = xp


    def asarray(obj, /, *, units=None, dtype=None, device=None, copy=None):
        if device is not None:
            raise NotImplementedError("`device` argument is not implemented")

        magnitude = getattr(obj, 'magnitude', obj)
        magnitude = xp.asarray(magnitude, dtype=dtype, device=device, copy=copy)

        units = getattr(obj, 'units', None) if units is None else units

        return ArrayUnitQuantity(magnitude, units, xp=xp)
    mod.asarray = asarray

    def sum(x, /, *, axis=None, dtype=None, keepdims=False):
        x = asarray(x)
        magnitude = xp.asarray(x.magnitude, copy=True)
        units = x.units
        magnitude = xp.sum(x, axis=axis, dtype=dtype, keepdims=keepdims)
        units = (1 * units + 1 * units).units
        return ArrayUnitQuantity(magnitude, units, xp=xp)
    mod.sum = sum

    def var(x, /, *, axis=None, correction=0.0, keepdims=False):
        x = asarray(x)
        magnitude = xp.asarray(x.magnitude, copy=True)
        units = x.units
        magnitude = xp.var(x, axis=axis, correction=correction, keepdims=keepdims)
        units = ((1 * units + 1 * units) ** 2).units
        return ArrayUnitQuantity(magnitude, units, xp=xp)
    mod.var = var

    return mod
