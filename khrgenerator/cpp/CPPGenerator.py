
import os, sys
from os.path import join as pjoin
import time
import re
from itertools import groupby

from jinja2 import Environment, PackageLoader, Template

from khrapi.BitfieldGroup import BitfieldGroup
from khrapi.Enumerator import Enumerator
from khrapi.Version import Version

class CPPGenerator:

    @classmethod
    def render(cls, engine, template, target, **kwargs):
        templateFilename = Template(template).render(**kwargs)
        targetFilename = Template(target).render(**kwargs)
        print("Generate %s" % (targetFilename))
        t = engine.get_template(templateFilename)
        t.stream(**kwargs).dump(targetFilename)

    @classmethod
    def generate(cls, profile, api):
        baseNamespace = profile.baseNamespace
        multiContextBinding = profile.multiContextBinding
        booleanWidth = profile.booleanWidth
        bindingNamespace = profile.bindingNamespace
        minCoreVersion = profile.minCoreVersion
        targetdir = profile.targetDir

        # TEMPLATE SETUP

        template_engine = Environment(loader=PackageLoader('khrgenerator.cpp', 'templates'))
        # print(template_engine.list_templates())

        # target directory structure

        includedir = pjoin(targetdir, pjoin(bindingNamespace, "include/" + bindingNamespace + "/"))
        includedir_api = pjoin(includedir, "{{profile.baseNamespace}}{{memberSet}}/")
        includedir_aux = pjoin(targetdir, pjoin(bindingNamespace + "-aux", "include/" + bindingNamespace + "-aux/"))
        sourcedir = pjoin(targetdir, pjoin(bindingNamespace, "source/"))
        sourcedir_api = pjoin(sourcedir, "{{profile.baseNamespace}}/")
        sourcedir_aux = pjoin(targetdir, pjoin(bindingNamespace + "-aux", "source/"))
        testdir = pjoin(targetdir, "tests/" + bindingNamespace + "-test/")

        # TEMPLATE APPLICATION

        # Generate files with common context

        # cls.render(template_engine, "revision.h.tpl", sourcedir_aux+"{{profile.baseNamespace}}revision.h", api=api, profile=profile)
        # cls.render(template_engine, "extension.h.tpl", includedir_api+"extension.h", api=api, profile=profile)
        # cls.render(template_engine, "values.h.tpl", includedir_api+"values.h", api=api, profile=profile,
        #     values=api.typeByIdentifier("SpecialValues")
        # )
#       # cls.render(template_engine, "types.h.tpl", includedir_api+"types.h", api=api, profile=profile)
        # cls.render(template_engine, "bitfield.h.tpl", includedir_api+"bitfield.h", api=api, profile=profile,
        #     groups=[ type for type in api.types if isinstance(type, BitfieldGroup) and len(type.values) > 0 ],
        #     constants=[ constant for constant in api.constants if len(constant.groups) > 0 and isinstance(constant.groups[0], BitfieldGroup) ],
        #     max_constant_length = str(max([ len(constant.identifier) for constant in api.constants if len(constant.groups) > 0 and isinstance(constant.groups[0], BitfieldGroup) ]))
        # )
        # cls.render(template_engine, "enum.h.tpl", includedir_api+"enum.h", api=api, profile=profile,
        #     groups=[ type for type in api.types if isinstance(type, Enumerator) and len(type.values) > 0 ],
        #     constants=[ constant for constant in api.constants if len(constant.groups) > 0 and isinstance(constant.groups[0], Enumerator) ],
        #     max_constant_length=str(max([ len(constant.identifier) for constant in api.constants if len(constant.groups) > 0 and isinstance(constant.groups[0], Enumerator) ]))
        # )
        # cls.render(template_engine, "functions.h.tpl", includedir_api+"functions.h", api=api, profile=profile,
        #     functions=[ function for function in api.functions ]
        # )
        # cls.render(template_engine, "{{profile.baseNamespace}}.h.tpl", includedir_api+"{{profile.baseNamespace}}.h", api=api, profile=profile)

        # cls.render(template_engine, "AllVersions_test.cpp.tpl", testdir+"AllVersions_test.cpp", api=api, profile=profile,
        #     versions=api.versions
        # )
        # cls.render(template_engine, "ValidVersions_list.cpp.tpl", sourcedir_aux+"ValidVersions_list.cpp", api=api, profile=profile,
        #     versions=[ version for version in api.versions if isinstance(version, Version) ]
        # )

        # cls.render(template_engine, "Meta.h.tpl", includedir_aux+"Meta.h", api=api, profile=profile,
        #     groups=[ type for type in api.types if isinstance(type, BitfieldGroup) and len(type.values) > 0 ]
        # )
        # cls.render(template_engine, "Meta_Maps.h.tpl", sourcedir_aux+"Meta_Maps.h", api=api, profile=profile,
        #     groups=[ type for type in api.types if isinstance(type, BitfieldGroup) and len(type.values) > 0 ]
        # )
        # cls.render(template_engine, "Meta_getStringByBitfield.cpp.tpl", sourcedir_aux+"Meta_getStringByBitfield.cpp", api=api, profile=profile,
        #     groups=[ type for type in api.types if isinstance(type, BitfieldGroup) and len(type.values) > 0 ]
        # )
        # cls.render(template_engine, "Meta_StringsByBitfield.cpp.tpl", sourcedir_aux+"Meta_StringsByBitfield.cpp", api=api, profile=profile,
        #     groups=[ type for type in api.types if isinstance(type, BitfieldGroup) and len(type.values) > 0 ]
        # )
        # cls.render(template_engine, "Meta_BitfieldsByString.cpp.tpl", sourcedir_aux+"Meta_BitfieldsByString.cpp", api=api, profile=profile,
        #     groups=cls.identifierPrefixGroups(api, [ constant for constant in api.constants if len(constant.groups) > 0 and isinstance(constant.groups[0], BitfieldGroup) ], 3)
        # )
        # cls.render(template_engine, "Meta_StringsByBoolean.cpp.tpl", sourcedir_aux+"Meta_StringsByBoolean.cpp", api=api, profile=profile,
        #     booleans=[api.constantByIdentifier("GL_TRUE"), api.constantByIdentifier("GL_FALSE")]
        # )
        # cls.render(template_engine, "Meta_BooleansByString.cpp.tpl", sourcedir_aux+"Meta_BooleansByString.cpp", api=api, profile=profile,
        #     booleans=[api.constantByIdentifier("GL_TRUE"), api.constantByIdentifier("GL_FALSE")]
        # )
        # cls.render(template_engine, "Meta_StringsByEnum.cpp.tpl", sourcedir_aux+"Meta_StringsByEnum.cpp", api=api, profile=profile,
        #     constants=[ constant for constant in api.constants if len(constant.groups) > 0 and isinstance(constant.groups[0], Enumerator) ]
        # )
        # cls.render(template_engine, "Meta_EnumsByString.cpp.tpl", sourcedir_aux+"Meta_EnumsByString.cpp", api=api, profile=profile,
        #     groups=cls.identifierPrefixGroups(api, [ constant for constant in api.constants if len(constant.groups) > 0 and isinstance(constant.groups[0], Enumerator) ], 3)
        # )
        # cls.render(template_engine, "Meta_StringsByExtension.cpp.tpl", sourcedir_aux+"Meta_StringsByExtension.cpp", api=api, profile=profile,
        #     extensions=api.extensions
        # )
        # cls.render(template_engine, "Meta_ExtensionsByString.cpp.tpl", sourcedir_aux+"Meta_ExtensionsByString.cpp", api=api, profile=profile,
        #     groups=cls.identifierPrefixGroups(api, api.extensions, 3)
        # )
        # cls.render(template_engine, "Meta_ReqVersionsByExtension.cpp.tpl", sourcedir_aux+"Meta_ReqVersionsByExtension.cpp", api=api, profile=profile,
        #     extensionsInCore=api.extensionsByCoreVersion()
        # )
        # cls.render(template_engine, "Meta_FunctionStringsByExtension.cpp.tpl", sourcedir_aux+"Meta_FunctionStringsByExtension.cpp", api=api, profile=profile,
        #     extensions=api.extensions
        # )
        # cls.render(template_engine, "Meta_FunctionStringsByVersion.cpp.tpl", sourcedir_aux+"Meta_FunctionStringsByVersion.cpp", api=api, profile=profile,
        #     versions=[ version for version in api.versions if isinstance(version, Version) ]
        # )
        cls.render(template_engine, "Meta_ExtensionsByFunctionString.cpp.tpl", sourcedir_aux+"Meta_ExtensionsByFunctionString.cpp", api=api, profile=profile,
            extensionsByFunction=cls.identifierPrefixGroupsDict(api, api.extensionsByFunction(), 2)
        )

        # TODO

        #Generator.generate(generalContext, pjoin(sourcedir_aux, "Meta_ExtensionsByFunctionString.cpp"))

        ## KHR binding

        #if multiContextBinding:
        #    Generator.generate(generalContext, pjoin(includedir, "Binding.h"), "khrbinding/MultiContextBinding.h")
        #    Generator.generate(generalContext, pjoin(sourcedir, "Binding.cpp"), "khrbinding/MultiContextBinding.cpp")
        #    Generator.generate(generalContext, pjoin(includedir, bindingNamespace + ".h"),
        #                       "khrbinding/multicontextinterface.h")
        #    Generator.generate(generalContext, pjoin(sourcedir, bindingNamespace + ".cpp"),
        #                       "khrbinding/multicontextinterface.cpp")
        #else:
        #    Generator.generate(generalContext, pjoin(includedir, "Binding.h"), "khrbinding/SingleContextBinding.h")
        #    Generator.generate(generalContext, pjoin(sourcedir, "Binding.cpp"), "khrbinding/SingleContextBinding.cpp")
        #    Generator.generate(generalContext, pjoin(includedir, bindingNamespace + ".h"),
        #                       "khrbinding/singlecontextinterface.h")
        #    Generator.generate(generalContext, pjoin(sourcedir, bindingNamespace + ".cpp"),
        #                       "khrbinding/singlecontextinterface.cpp")

        #Generator.generate(generalContext, pjoin(sourcedir, "Binding_list.cpp"))

        #if booleanWidth == 8:
        #    Generator.generate(generalContext, pjoin(includedir, "Boolean8.h"), "khrbinding/Boolean8.h")
        #    Generator.generate(generalContext, pjoin(includedir, "Boolean8.inl"), "khrbinding/Boolean8.inl")
        #else:
        #    Generator.generate(generalContext, pjoin(includedir, "Boolean32.h"), "khrbinding/Boolean32.h")
        #    Generator.generate(generalContext, pjoin(includedir, "Boolean32.inl"), "khrbinding/Boolean32.inl")

        #Generator.generate(generalContext, pjoin(includedir, "AbstractFunction.h"), "khrbinding/AbstractFunction.h")
        #Generator.generate(generalContext, pjoin(includedir, "AbstractState.h"), "khrbinding/AbstractState.h")
        #Generator.generate(generalContext, pjoin(includedir, "AbstractValue.h"), "khrbinding/AbstractValue.h")
        #Generator.generate(generalContext, pjoin(includedir, "CallbackMask.h"), "khrbinding/CallbackMask.h")
        #Generator.generate(generalContext, pjoin(includedir, "CallbackMask.inl"), "khrbinding/CallbackMask.inl")
        #Generator.generate(generalContext, pjoin(includedir, "ContextHandle.h"), "khrbinding/ContextHandle.h")
        #Generator.generate(generalContext, pjoin(includedir, "Function.h"), "khrbinding/Function.h")
        #Generator.generate(generalContext, pjoin(includedir, "Function.inl"), "khrbinding/Function.inl")
        #Generator.generate(generalContext, pjoin(includedir, "FunctionCall.h"), "khrbinding/FunctionCall.h")
        #Generator.generate(generalContext, pjoin(includedir, "ProcAddress.h"), "khrbinding/ProcAddress.h")
        #Generator.generate(generalContext, pjoin(includedir, "SharedBitfield.h"), "khrbinding/SharedBitfield.h")
        #Generator.generate(generalContext, pjoin(includedir, "SharedBitfield.inl"), "khrbinding/SharedBitfield.inl")
        #Generator.generate(generalContext, pjoin(includedir, "State.h"), "khrbinding/State.h")
        #Generator.generate(generalContext, pjoin(includedir, "Value.h"), "khrbinding/Value.h")
        #Generator.generate(generalContext, pjoin(includedir, "Value.inl"), "khrbinding/Value.inl")
        #Generator.generate(generalContext, pjoin(includedir, "Version.h"), "khrbinding/Version.h")
        #Generator.generate(generalContext, pjoin(includedir, "Version.inl"), "khrbinding/Version.inl")

        #Generator.generate(generalContext, pjoin(sourcedir, "AbstractFunction.cpp"), "khrbinding/AbstractFunction.cpp")
        #Generator.generate(generalContext, pjoin(sourcedir, "AbstractState.cpp"), "khrbinding/AbstractState.cpp")
        #Generator.generate(generalContext, pjoin(sourcedir, "AbstractValue.cpp"), "khrbinding/AbstractValue.cpp")
        #Generator.generate(generalContext, pjoin(sourcedir, "FunctionCall.cpp"), "khrbinding/FunctionCall.cpp")
        #Generator.generate(generalContext, pjoin(sourcedir, "State.cpp"), "khrbinding/State.cpp")

        ## KHR binding AUX

        #Generator.generate(generalContext, pjoin(includedir_aux, "RingBuffer.h"), "khrbinding-aux/RingBuffer.h")
        #Generator.generate(generalContext, pjoin(includedir_aux, "RingBuffer.inl"), "khrbinding-aux/RingBuffer.inl")
        #Generator.generate(generalContext, pjoin(includedir_aux, "types_to_string.h"),
        #                   "khrbinding-aux/types_to_string.h")
        #Generator.generate(generalContext, pjoin(includedir_aux, "types_to_string.inl"),
        #                   "khrbinding-aux/types_to_string.inl")
        #Generator.generate(generalContext, pjoin(includedir_aux, "ValidVersions.h"), "khrbinding-aux/ValidVersions.h")

        #Generator.generate(generalContext, pjoin(sourcedir_aux, "ValidVersions.cpp"),
        #                   "khrbinding-aux/ValidVersions.cpp")
        #Generator.generate(generalContext, pjoin(sourcedir_aux, "types_to_string.cpp"),
        #                   "khrbinding-aux/types_to_string.cpp")

        ## Generate function-related files with specific contexts for each initial letter of the function name
        #for functionGroup in generalContext["functionsByInitial"]["groups"]:
        #    specificContext = generalContext.copy()
        #    specificContext["currentFunctionGroup"] = functionGroup
        #    specificContext["currentFunctionInitial"] = functionGroup["name"].lower()

        #    Generator.generate(specificContext, pjoin(sourcedir_api, "functions_{currentFunctionInitial}.cpp"),
        #                       "functions.cpp")
        #    Generator.generate(specificContext, pjoin(sourcedir, "Binding_objects_{currentFunctionInitial}.cpp"),
        #                       "Binding_objects.cpp")

        ## Generate files with ApiMemberSet-specific contexts
        #for feature, core, ext in context.apiMemberSets():
        #    specificContext = context.apiMemberSetSpecific(feature, core, ext)

        #    Generator.generate(specificContext, pjoin(includedir_api, "boolean.h"), "booleanF.h")
        #    Generator.generate(specificContext, pjoin(includedir_api, "values.h"), "valuesF.h")
        #    Generator.generate(specificContext, pjoin(includedir_api, "types.h"), "typesF.h")
        #    Generator.generate(specificContext, pjoin(includedir_api, "bitfield.h"), "bitfieldF.h")
        #    Generator.generate(specificContext, pjoin(includedir_api, "enum.h"), "enumF.h")
        #    Generator.generate(specificContext, pjoin(includedir_api, "functions.h"), "functionsF.h")
        #    Generator.generate(specificContext, pjoin(includedir_api, "{api}.h"), "{api}F.h")

    @classmethod
    def identifierPrefixGroups(cls, api, values, lookupOffset):
        result = { chr(alpha):[] for alpha in range(ord('A'), ord('Z')+1) }
        result["0"] = []
        for value in values:
            result[value.identifier[lookupOffset].upper() if value.identifier[lookupOffset].isalpha() else '0'].append(value)
        return result

    @classmethod
    def identifierPrefixGroupsDict(cls, api, dictionary, lookupOffset):
        result = { chr(alpha):{} for alpha in range(ord('A'), ord('Z')+1) }
        result["0"] = {}
        for key, values in dictionary.items():
            result[key.identifier[lookupOffset].upper() if key.identifier[lookupOffset].isalpha() else '0'][key] = values
        return result
