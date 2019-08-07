
#pragma once


#include <{{api}}binding/no{{api}}.h>
#include <{{api}}binding/{{api}}binding_api.h>
#include <{{api}}binding/{{api}}binding_features.h>
#include <{{api}}binding/{{api}}/boolean.h>

#include <cstddef>
#include <cstdint>
#include <array>
{{additionalTypeIncludes}}

#include <string>


#ifdef _MSC_VER
#define {{ucapi}}_APIENTRY __stdcall
#else
#define {{ucapi}}_APIENTRY
#endif


namespace {{api}}
{

{{additionalTypes}}
{{#types.items}}
{{item.definition}}
{{/types.items}}

} // namespace {{api}}


// Type Integrations

{{#types.items}}
{{#item.integrations.hashable}}
{{#item}}{{>partials/types_hashable.h}}{{/item}}

{{/item.integrations.hashable}}
{{#item.integrations.addable}}
{{#item}}{{>partials/types_addable.h}}{{/item}}

{{/item.integrations.addable}}
{{#item.integrations.bitOperatable}}
{{#item}}{{>partials/types_bitOperatable.h}}{{/item}}

{{/item.integrations.bitOperatable}}
{{#item.integrations.comparable}}
{{#item}}{{>partials/types_comparable.h}}{{/item}}

{{/item.integrations.comparable}}
{{/types.items}}
