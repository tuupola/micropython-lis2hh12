# Changelog

All notable changes to this project will be documented in this file, in reverse chronological order by release.

## [0.3.0](https://github.com/tuupola/micropython-lis2hh12/compare/0.2.0...master) - 2024-02-24
### Added
- Support for LIS2DH12 ([#3](https://github.com/tuupola/micropython-lis2hh12/pull/3)).
### Fixed
- The `with` statement now works ([#a4f60bc](https://github.com/tuupola/micropython-lis2hh12/commit/a4f60bc8bff1f84b370e85bc4542c7a2d51732ad)).
    ```
    with LIS2HH12(i2c) as sensor:
        print(sensor.acceleration)
    ```

## [0.2.0](https://github.com/tuupola/micropython-lis2hh12/compare/0.1.0...0.2.0) - 2018-02-10
### Changed
- Acceleration values are accessed as a property `sensor.acceleration` instead of function `sensor.acceleration()`.
- By default sensor values are now returned as `m/s^2` instead of `g`.

### Added
- Constructor parameter `sf=SF_G` which changes the sensor values to be in `g`.

## 0.1.0 - 2017-10-04

Initial working release.