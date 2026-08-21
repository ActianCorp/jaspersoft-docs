---
title: The license information Service
description: "The RESTful API provides access to the feature flags tied to a JasperReports Server license. It enables the user to query the availability of licensed features such as Multi-Tenancy, Ad Hoc Designer,..."
---

# The license information Service

The RESTful API provides access to the feature flags tied to a JasperReports Server license. It enables the user to query the availability of licensed features such as Multi-Tenancy, Ad Hoc Designer, Dashboard Designer, Visualize.js, and more.

| Property | Details |
|----|----|
| Base URL | http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/licenseFeatures |
| Authentication | HTTP Basic Auth (Only accessible to superuser and jasperadmin) |
| Content-Type | JSON |
| API Version | v2 |

- All endpoint requires the basic authentication.

  `Username: superuser or jasperadmin`

  `Password: superuser or jasperadmin`

## Endpoints

1.  Get all license features

    | Method | URL |
    |----|----|
    | GET | http://\<host\>:\<port\>/jasperserver\[-pro\]/rest_v2/licenseFeatures |
    | **Return Value on the Success** | **Typical Return Values on Failure** |
    | 200 OK: Body described below |   |

    The server returns a structure containing the information:

    ``` json
    {"mt": true,"cl": true,"al": false,...}
    ```

2.  Get Individual License Feature Status

    GET `/licenseFeatures/{featureCode}`

    | Feature | Endpoint | Feature code |
    |----|----|----|
    | Multi-Tenancy | `/licenseFeatures/mt ` | mt |
    | Clustering | `/licenseFeatures/cl ` | cl |
    | Altering | `/licenseFeatures/al ` | al |
    | Data Snapshot | `/licenseFeatures/ds ` | ds |
    | Fusion | `/licenseFeatures/fusion ` | fusion |
    | Report Bursting | `/licenseFeatures/rb ` | rb |
    | Audit | `/licenseFeatures/aud ` | aud |
    | Data Virtualizer | `/licenseFeatures/dv` | dv |
    | Visualize.js | `/licenseFeatures/vj` | vj |
    | OLAP / Analysis | `/licenseFeatures/ana` | ana |
    | White Labeling | `/licenseFeatures/wl ` | wl |
    | Ad hoc Designer | `/licenseFeatures/ahd ` | ahd |
    | Dashboard Designer | `/licenseFeatures/db ` | db |
    | **Return Value on Success** | **Typical Return Values on Failure** |   |
    | 200 OK: Body described below |   |   |

    ``` json
    {"mt": true}
    ```

3.  Invalid Feature Check

    | Method | URL |
    |----|----|
    | GET | `/licenseFeatures/Explore` or `/licenseFeatures/exp` |
    | **Return Value on Success** | **Typical Return Values on Failure** |
    | 404 Not Found: Body described below |   |

    ``` json
    {"message": "Requested License Feature <feature> is not supported","errorCode": "resource.not.found"}
    ```

!!! note

    - All feature flags return a boolean.

    - All feature flags are case insensitive.

    - The licenseFeatures API is only accessible to `superuser` and `jasperadmin` users and for the rest of the user the API throws 401 unauthorized error.
