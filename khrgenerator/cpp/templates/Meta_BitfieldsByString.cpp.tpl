
#include "Meta_Maps.h"

#include <{{api}}binding/{{api}}/bitfield.h>


using namespace {{api}};


namespace {{api}}binding { namespace aux
{


{{#bitfieldsByInitial.groups}}
{{#empty}}
const std::unordered_map<std::string, {{bitfieldType}}> Meta_BitfieldsByString_{{name}}{};
{{/empty}}
{{^empty}}
const std::unordered_map<std::string, {{bitfieldType}}> Meta_BitfieldsByString_{{name}} =
{
{{#items}}
    { "{{item.name}}", static_cast<{{bitfieldType}}>({{item.primaryGroup}}::{{item.identifier}}) }{{^last}},{{/last}}
{{/items}}
};
{{/empty}}

{{/bitfieldsByInitial.groups}}
const std::array<std::unordered_map<std::string, {{bitfieldType}}>, {{bitfieldsByInitial.count}}> Meta_BitfieldsByStringMaps =
{ {
{{#bitfieldsByInitial.groups}}
    Meta_BitfieldsByString_{{name}}{{^last}},{{/last}}
{{/bitfieldsByInitial.groups}}
} };


} } // namespace {{api}}binding::aux
