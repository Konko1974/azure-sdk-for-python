# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Association
    from ._models_py3 import CustomRPActionRouteDefinition
    from ._models_py3 import CustomRPManifest
    from ._models_py3 import CustomRPResourceTypeRouteDefinition
    from ._models_py3 import CustomRPRouteDefinition
    from ._models_py3 import CustomRPValidations
    from ._models_py3 import ErrorDefinition
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import Resource
    from ._models_py3 import ResourceProviderOperation
    from ._models_py3 import ResourceProviderOperationDisplay
    from ._models_py3 import ResourceProvidersUpdate
except (SyntaxError, ImportError):
    from ._models import Association
    from ._models import CustomRPActionRouteDefinition
    from ._models import CustomRPManifest
    from ._models import CustomRPResourceTypeRouteDefinition
    from ._models import CustomRPRouteDefinition
    from ._models import CustomRPValidations
    from ._models import ErrorDefinition
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import Resource
    from ._models import ResourceProviderOperation
    from ._models import ResourceProviderOperationDisplay
    from ._models import ResourceProvidersUpdate
from ._paged_models import AssociationPaged
from ._paged_models import CustomRPManifestPaged
from ._paged_models import ResourceProviderOperationPaged
from ._customproviders_client_enums import (
    ActionRouting,
    ResourceTypeRouting,
    ValidationType,
    ProvisioningState,
)

__all__ = [
    'Association',
    'CustomRPActionRouteDefinition',
    'CustomRPManifest',
    'CustomRPResourceTypeRouteDefinition',
    'CustomRPRouteDefinition',
    'CustomRPValidations',
    'ErrorDefinition',
    'ErrorResponse', 'ErrorResponseException',
    'Resource',
    'ResourceProviderOperation',
    'ResourceProviderOperationDisplay',
    'ResourceProvidersUpdate',
    'ResourceProviderOperationPaged',
    'CustomRPManifestPaged',
    'AssociationPaged',
    'ActionRouting',
    'ResourceTypeRouting',
    'ValidationType',
    'ProvisioningState',
]
