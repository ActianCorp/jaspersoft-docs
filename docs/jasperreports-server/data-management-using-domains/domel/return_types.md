---
title: Return Types
description: "DomEL expressions are used in different contexts for different purposes. The expected return type depends on where the expression appears:"
---

# Return Types

DomEL expressions are used in different contexts for different purposes. The expected return type depends on where the expression appears:

| Appears In | Expected Return Type | Explanation |
|----|----|----|
| Join expression | Boolean | Within a join expression, the `on` clause contains a comparison of fields from each table that has a boolean result. The `on` clause may also contain other DomEL expressions logically associated with `and` or `or` to create a complex join condition. |
| Calculated field | any type | The expression must evaluate to a type that is compatible with the SQL type declared in the Domain Designer or in the design file. For example, if the declared type is `java.lang.Float`, the expression must compute a decimal value. |
| Pre-filter | Boolean | Filters must be true or false overall. When there are several conditions, they must be logically associated with `and` or `or` (currently, only `and` is supported in the Domain Designer). |
