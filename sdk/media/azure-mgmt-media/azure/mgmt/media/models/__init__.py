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
    from ._models_py3 import AacAudio
    from ._models_py3 import AbsoluteClipTime
    from ._models_py3 import AccountFilter
    from ._models_py3 import AkamaiAccessControl
    from ._models_py3 import AkamaiSignatureHeaderAuthenticationKey
    from ._models_py3 import ApiError, ApiErrorException
    from ._models_py3 import Asset
    from ._models_py3 import AssetContainerSas
    from ._models_py3 import AssetFileEncryptionMetadata
    from ._models_py3 import AssetFilter
    from ._models_py3 import AssetStreamingLocator
    from ._models_py3 import Audio
    from ._models_py3 import AudioAnalyzerPreset
    from ._models_py3 import AudioOverlay
    from ._models_py3 import BuiltInStandardEncoderPreset
    from ._models_py3 import CbcsDrmConfiguration
    from ._models_py3 import CencDrmConfiguration
    from ._models_py3 import CheckNameAvailabilityInput
    from ._models_py3 import ClipTime
    from ._models_py3 import Codec
    from ._models_py3 import CommonEncryptionCbcs
    from ._models_py3 import CommonEncryptionCenc
    from ._models_py3 import ContentKeyPolicy
    from ._models_py3 import ContentKeyPolicyClearKeyConfiguration
    from ._models_py3 import ContentKeyPolicyConfiguration
    from ._models_py3 import ContentKeyPolicyFairPlayConfiguration
    from ._models_py3 import ContentKeyPolicyFairPlayOfflineRentalConfiguration
    from ._models_py3 import ContentKeyPolicyOpenRestriction
    from ._models_py3 import ContentKeyPolicyOption
    from ._models_py3 import ContentKeyPolicyPlayReadyConfiguration
    from ._models_py3 import ContentKeyPolicyPlayReadyContentEncryptionKeyFromHeader
    from ._models_py3 import ContentKeyPolicyPlayReadyContentEncryptionKeyFromKeyIdentifier
    from ._models_py3 import ContentKeyPolicyPlayReadyContentKeyLocation
    from ._models_py3 import ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction
    from ._models_py3 import ContentKeyPolicyPlayReadyLicense
    from ._models_py3 import ContentKeyPolicyPlayReadyPlayRight
    from ._models_py3 import ContentKeyPolicyProperties
    from ._models_py3 import ContentKeyPolicyRestriction
    from ._models_py3 import ContentKeyPolicyRestrictionTokenKey
    from ._models_py3 import ContentKeyPolicyRsaTokenKey
    from ._models_py3 import ContentKeyPolicySymmetricTokenKey
    from ._models_py3 import ContentKeyPolicyTokenClaim
    from ._models_py3 import ContentKeyPolicyTokenRestriction
    from ._models_py3 import ContentKeyPolicyUnknownConfiguration
    from ._models_py3 import ContentKeyPolicyUnknownRestriction
    from ._models_py3 import ContentKeyPolicyWidevineConfiguration
    from ._models_py3 import ContentKeyPolicyX509CertificateTokenKey
    from ._models_py3 import CopyAudio
    from ._models_py3 import CopyVideo
    from ._models_py3 import CrossSiteAccessPolicies
    from ._models_py3 import DefaultKey
    from ._models_py3 import Deinterlace
    from ._models_py3 import EnabledProtocols
    from ._models_py3 import EntityNameAvailabilityCheckOutput
    from ._models_py3 import EnvelopeEncryption
    from ._models_py3 import FaceDetectorPreset
    from ._models_py3 import Filters
    from ._models_py3 import FilterTrackPropertyCondition
    from ._models_py3 import FilterTrackSelection
    from ._models_py3 import FirstQuality
    from ._models_py3 import Format
    from ._models_py3 import H264Layer
    from ._models_py3 import H264Video
    from ._models_py3 import Hls
    from ._models_py3 import Image
    from ._models_py3 import ImageFormat
    from ._models_py3 import IPAccessControl
    from ._models_py3 import IPRange
    from ._models_py3 import Job
    from ._models_py3 import JobError
    from ._models_py3 import JobErrorDetail
    from ._models_py3 import JobInput
    from ._models_py3 import JobInputAsset
    from ._models_py3 import JobInputClip
    from ._models_py3 import JobInputHttp
    from ._models_py3 import JobInputs
    from ._models_py3 import JobOutput
    from ._models_py3 import JobOutputAsset
    from ._models_py3 import JpgFormat
    from ._models_py3 import JpgImage
    from ._models_py3 import JpgLayer
    from ._models_py3 import Layer
    from ._models_py3 import ListContainerSasInput
    from ._models_py3 import ListContentKeysResponse
    from ._models_py3 import ListPathsResponse
    from ._models_py3 import ListStreamingLocatorsResponse
    from ._models_py3 import LiveEvent
    from ._models_py3 import LiveEventActionInput
    from ._models_py3 import LiveEventEncoding
    from ._models_py3 import LiveEventEndpoint
    from ._models_py3 import LiveEventInput
    from ._models_py3 import LiveEventInputAccessControl
    from ._models_py3 import LiveEventPreview
    from ._models_py3 import LiveEventPreviewAccessControl
    from ._models_py3 import LiveOutput
    from ._models_py3 import Location
    from ._models_py3 import MediaService
    from ._models_py3 import Metric
    from ._models_py3 import MetricDimension
    from ._models_py3 import MetricProperties
    from ._models_py3 import Mp4Format
    from ._models_py3 import MultiBitrateFormat
    from ._models_py3 import NoEncryption
    from ._models_py3 import ODataError
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OutputFile
    from ._models_py3 import Overlay
    from ._models_py3 import PngFormat
    from ._models_py3 import PngImage
    from ._models_py3 import PngLayer
    from ._models_py3 import PresentationTimeRange
    from ._models_py3 import Preset
    from ._models_py3 import Provider
    from ._models_py3 import ProxyResource
    from ._models_py3 import Rectangle
    from ._models_py3 import Resource
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import StandardEncoderPreset
    from ._models_py3 import StorageAccount
    from ._models_py3 import StorageEncryptedAssetDecryptionData
    from ._models_py3 import StreamingEndpoint
    from ._models_py3 import StreamingEndpointAccessControl
    from ._models_py3 import StreamingEntityScaleUnit
    from ._models_py3 import StreamingLocator
    from ._models_py3 import StreamingLocatorContentKey
    from ._models_py3 import StreamingPath
    from ._models_py3 import StreamingPolicy
    from ._models_py3 import StreamingPolicyContentKey
    from ._models_py3 import StreamingPolicyContentKeys
    from ._models_py3 import StreamingPolicyFairPlayConfiguration
    from ._models_py3 import StreamingPolicyPlayReadyConfiguration
    from ._models_py3 import StreamingPolicyWidevineConfiguration
    from ._models_py3 import SubscriptionMediaService
    from ._models_py3 import SyncStorageKeysInput
    from ._models_py3 import TrackedResource
    from ._models_py3 import TrackPropertyCondition
    from ._models_py3 import TrackSelection
    from ._models_py3 import Transform
    from ._models_py3 import TransformOutput
    from ._models_py3 import TransportStreamFormat
    from ._models_py3 import Video
    from ._models_py3 import VideoAnalyzerPreset
    from ._models_py3 import VideoLayer
    from ._models_py3 import VideoOverlay
except (SyntaxError, ImportError):
    from ._models import AacAudio
    from ._models import AbsoluteClipTime
    from ._models import AccountFilter
    from ._models import AkamaiAccessControl
    from ._models import AkamaiSignatureHeaderAuthenticationKey
    from ._models import ApiError, ApiErrorException
    from ._models import Asset
    from ._models import AssetContainerSas
    from ._models import AssetFileEncryptionMetadata
    from ._models import AssetFilter
    from ._models import AssetStreamingLocator
    from ._models import Audio
    from ._models import AudioAnalyzerPreset
    from ._models import AudioOverlay
    from ._models import BuiltInStandardEncoderPreset
    from ._models import CbcsDrmConfiguration
    from ._models import CencDrmConfiguration
    from ._models import CheckNameAvailabilityInput
    from ._models import ClipTime
    from ._models import Codec
    from ._models import CommonEncryptionCbcs
    from ._models import CommonEncryptionCenc
    from ._models import ContentKeyPolicy
    from ._models import ContentKeyPolicyClearKeyConfiguration
    from ._models import ContentKeyPolicyConfiguration
    from ._models import ContentKeyPolicyFairPlayConfiguration
    from ._models import ContentKeyPolicyFairPlayOfflineRentalConfiguration
    from ._models import ContentKeyPolicyOpenRestriction
    from ._models import ContentKeyPolicyOption
    from ._models import ContentKeyPolicyPlayReadyConfiguration
    from ._models import ContentKeyPolicyPlayReadyContentEncryptionKeyFromHeader
    from ._models import ContentKeyPolicyPlayReadyContentEncryptionKeyFromKeyIdentifier
    from ._models import ContentKeyPolicyPlayReadyContentKeyLocation
    from ._models import ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction
    from ._models import ContentKeyPolicyPlayReadyLicense
    from ._models import ContentKeyPolicyPlayReadyPlayRight
    from ._models import ContentKeyPolicyProperties
    from ._models import ContentKeyPolicyRestriction
    from ._models import ContentKeyPolicyRestrictionTokenKey
    from ._models import ContentKeyPolicyRsaTokenKey
    from ._models import ContentKeyPolicySymmetricTokenKey
    from ._models import ContentKeyPolicyTokenClaim
    from ._models import ContentKeyPolicyTokenRestriction
    from ._models import ContentKeyPolicyUnknownConfiguration
    from ._models import ContentKeyPolicyUnknownRestriction
    from ._models import ContentKeyPolicyWidevineConfiguration
    from ._models import ContentKeyPolicyX509CertificateTokenKey
    from ._models import CopyAudio
    from ._models import CopyVideo
    from ._models import CrossSiteAccessPolicies
    from ._models import DefaultKey
    from ._models import Deinterlace
    from ._models import EnabledProtocols
    from ._models import EntityNameAvailabilityCheckOutput
    from ._models import EnvelopeEncryption
    from ._models import FaceDetectorPreset
    from ._models import Filters
    from ._models import FilterTrackPropertyCondition
    from ._models import FilterTrackSelection
    from ._models import FirstQuality
    from ._models import Format
    from ._models import H264Layer
    from ._models import H264Video
    from ._models import Hls
    from ._models import Image
    from ._models import ImageFormat
    from ._models import IPAccessControl
    from ._models import IPRange
    from ._models import Job
    from ._models import JobError
    from ._models import JobErrorDetail
    from ._models import JobInput
    from ._models import JobInputAsset
    from ._models import JobInputClip
    from ._models import JobInputHttp
    from ._models import JobInputs
    from ._models import JobOutput
    from ._models import JobOutputAsset
    from ._models import JpgFormat
    from ._models import JpgImage
    from ._models import JpgLayer
    from ._models import Layer
    from ._models import ListContainerSasInput
    from ._models import ListContentKeysResponse
    from ._models import ListPathsResponse
    from ._models import ListStreamingLocatorsResponse
    from ._models import LiveEvent
    from ._models import LiveEventActionInput
    from ._models import LiveEventEncoding
    from ._models import LiveEventEndpoint
    from ._models import LiveEventInput
    from ._models import LiveEventInputAccessControl
    from ._models import LiveEventPreview
    from ._models import LiveEventPreviewAccessControl
    from ._models import LiveOutput
    from ._models import Location
    from ._models import MediaService
    from ._models import Metric
    from ._models import MetricDimension
    from ._models import MetricProperties
    from ._models import Mp4Format
    from ._models import MultiBitrateFormat
    from ._models import NoEncryption
    from ._models import ODataError
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import OutputFile
    from ._models import Overlay
    from ._models import PngFormat
    from ._models import PngImage
    from ._models import PngLayer
    from ._models import PresentationTimeRange
    from ._models import Preset
    from ._models import Provider
    from ._models import ProxyResource
    from ._models import Rectangle
    from ._models import Resource
    from ._models import ServiceSpecification
    from ._models import StandardEncoderPreset
    from ._models import StorageAccount
    from ._models import StorageEncryptedAssetDecryptionData
    from ._models import StreamingEndpoint
    from ._models import StreamingEndpointAccessControl
    from ._models import StreamingEntityScaleUnit
    from ._models import StreamingLocator
    from ._models import StreamingLocatorContentKey
    from ._models import StreamingPath
    from ._models import StreamingPolicy
    from ._models import StreamingPolicyContentKey
    from ._models import StreamingPolicyContentKeys
    from ._models import StreamingPolicyFairPlayConfiguration
    from ._models import StreamingPolicyPlayReadyConfiguration
    from ._models import StreamingPolicyWidevineConfiguration
    from ._models import SubscriptionMediaService
    from ._models import SyncStorageKeysInput
    from ._models import TrackedResource
    from ._models import TrackPropertyCondition
    from ._models import TrackSelection
    from ._models import Transform
    from ._models import TransformOutput
    from ._models import TransportStreamFormat
    from ._models import Video
    from ._models import VideoAnalyzerPreset
    from ._models import VideoLayer
    from ._models import VideoOverlay
from ._paged_models import AccountFilterPaged
from ._paged_models import AssetFilterPaged
from ._paged_models import AssetPaged
from ._paged_models import ContentKeyPolicyPaged
from ._paged_models import JobPaged
from ._paged_models import LiveEventPaged
from ._paged_models import LiveOutputPaged
from ._paged_models import MediaServicePaged
from ._paged_models import OperationPaged
from ._paged_models import StreamingEndpointPaged
from ._paged_models import StreamingLocatorPaged
from ._paged_models import StreamingPolicyPaged
from ._paged_models import SubscriptionMediaServicePaged
from ._paged_models import TransformPaged
from ._azure_media_services_enums import (
    FilterTrackPropertyType,
    FilterTrackPropertyCompareOperation,
    MetricUnit,
    MetricAggregationType,
    StorageAccountType,
    AssetStorageEncryptionFormat,
    AssetContainerPermission,
    ContentKeyPolicyPlayReadyUnknownOutputPassingOption,
    ContentKeyPolicyPlayReadyLicenseType,
    ContentKeyPolicyPlayReadyContentType,
    ContentKeyPolicyRestrictionTokenType,
    ContentKeyPolicyFairPlayRentalAndLeaseKeyType,
    AacAudioProfile,
    AnalysisResolution,
    StretchMode,
    DeinterlaceParity,
    DeinterlaceMode,
    Rotation,
    H264VideoProfile,
    EntropyMode,
    H264Complexity,
    EncoderNamedPreset,
    InsightsType,
    OnErrorType,
    Priority,
    JobErrorCode,
    JobErrorCategory,
    JobRetry,
    JobState,
    TrackPropertyType,
    TrackPropertyCompareOperation,
    StreamingLocatorContentKeyType,
    StreamingPolicyStreamingProtocol,
    EncryptionScheme,
    LiveOutputResourceState,
    LiveEventInputProtocol,
    LiveEventEncodingType,
    LiveEventResourceState,
    StreamOptionsFlag,
    StreamingEndpointResourceState,
)

__all__ = [
    'AacAudio',
    'AbsoluteClipTime',
    'AccountFilter',
    'AkamaiAccessControl',
    'AkamaiSignatureHeaderAuthenticationKey',
    'ApiError', 'ApiErrorException',
    'Asset',
    'AssetContainerSas',
    'AssetFileEncryptionMetadata',
    'AssetFilter',
    'AssetStreamingLocator',
    'Audio',
    'AudioAnalyzerPreset',
    'AudioOverlay',
    'BuiltInStandardEncoderPreset',
    'CbcsDrmConfiguration',
    'CencDrmConfiguration',
    'CheckNameAvailabilityInput',
    'ClipTime',
    'Codec',
    'CommonEncryptionCbcs',
    'CommonEncryptionCenc',
    'ContentKeyPolicy',
    'ContentKeyPolicyClearKeyConfiguration',
    'ContentKeyPolicyConfiguration',
    'ContentKeyPolicyFairPlayConfiguration',
    'ContentKeyPolicyFairPlayOfflineRentalConfiguration',
    'ContentKeyPolicyOpenRestriction',
    'ContentKeyPolicyOption',
    'ContentKeyPolicyPlayReadyConfiguration',
    'ContentKeyPolicyPlayReadyContentEncryptionKeyFromHeader',
    'ContentKeyPolicyPlayReadyContentEncryptionKeyFromKeyIdentifier',
    'ContentKeyPolicyPlayReadyContentKeyLocation',
    'ContentKeyPolicyPlayReadyExplicitAnalogTelevisionRestriction',
    'ContentKeyPolicyPlayReadyLicense',
    'ContentKeyPolicyPlayReadyPlayRight',
    'ContentKeyPolicyProperties',
    'ContentKeyPolicyRestriction',
    'ContentKeyPolicyRestrictionTokenKey',
    'ContentKeyPolicyRsaTokenKey',
    'ContentKeyPolicySymmetricTokenKey',
    'ContentKeyPolicyTokenClaim',
    'ContentKeyPolicyTokenRestriction',
    'ContentKeyPolicyUnknownConfiguration',
    'ContentKeyPolicyUnknownRestriction',
    'ContentKeyPolicyWidevineConfiguration',
    'ContentKeyPolicyX509CertificateTokenKey',
    'CopyAudio',
    'CopyVideo',
    'CrossSiteAccessPolicies',
    'DefaultKey',
    'Deinterlace',
    'EnabledProtocols',
    'EntityNameAvailabilityCheckOutput',
    'EnvelopeEncryption',
    'FaceDetectorPreset',
    'Filters',
    'FilterTrackPropertyCondition',
    'FilterTrackSelection',
    'FirstQuality',
    'Format',
    'H264Layer',
    'H264Video',
    'Hls',
    'Image',
    'ImageFormat',
    'IPAccessControl',
    'IPRange',
    'Job',
    'JobError',
    'JobErrorDetail',
    'JobInput',
    'JobInputAsset',
    'JobInputClip',
    'JobInputHttp',
    'JobInputs',
    'JobOutput',
    'JobOutputAsset',
    'JpgFormat',
    'JpgImage',
    'JpgLayer',
    'Layer',
    'ListContainerSasInput',
    'ListContentKeysResponse',
    'ListPathsResponse',
    'ListStreamingLocatorsResponse',
    'LiveEvent',
    'LiveEventActionInput',
    'LiveEventEncoding',
    'LiveEventEndpoint',
    'LiveEventInput',
    'LiveEventInputAccessControl',
    'LiveEventPreview',
    'LiveEventPreviewAccessControl',
    'LiveOutput',
    'Location',
    'MediaService',
    'Metric',
    'MetricDimension',
    'MetricProperties',
    'Mp4Format',
    'MultiBitrateFormat',
    'NoEncryption',
    'ODataError',
    'Operation',
    'OperationDisplay',
    'OutputFile',
    'Overlay',
    'PngFormat',
    'PngImage',
    'PngLayer',
    'PresentationTimeRange',
    'Preset',
    'Provider',
    'ProxyResource',
    'Rectangle',
    'Resource',
    'ServiceSpecification',
    'StandardEncoderPreset',
    'StorageAccount',
    'StorageEncryptedAssetDecryptionData',
    'StreamingEndpoint',
    'StreamingEndpointAccessControl',
    'StreamingEntityScaleUnit',
    'StreamingLocator',
    'StreamingLocatorContentKey',
    'StreamingPath',
    'StreamingPolicy',
    'StreamingPolicyContentKey',
    'StreamingPolicyContentKeys',
    'StreamingPolicyFairPlayConfiguration',
    'StreamingPolicyPlayReadyConfiguration',
    'StreamingPolicyWidevineConfiguration',
    'SubscriptionMediaService',
    'SyncStorageKeysInput',
    'TrackedResource',
    'TrackPropertyCondition',
    'TrackSelection',
    'Transform',
    'TransformOutput',
    'TransportStreamFormat',
    'Video',
    'VideoAnalyzerPreset',
    'VideoLayer',
    'VideoOverlay',
    'AccountFilterPaged',
    'OperationPaged',
    'MediaServicePaged',
    'SubscriptionMediaServicePaged',
    'AssetPaged',
    'AssetFilterPaged',
    'ContentKeyPolicyPaged',
    'TransformPaged',
    'JobPaged',
    'StreamingPolicyPaged',
    'StreamingLocatorPaged',
    'LiveEventPaged',
    'LiveOutputPaged',
    'StreamingEndpointPaged',
    'FilterTrackPropertyType',
    'FilterTrackPropertyCompareOperation',
    'MetricUnit',
    'MetricAggregationType',
    'StorageAccountType',
    'AssetStorageEncryptionFormat',
    'AssetContainerPermission',
    'ContentKeyPolicyPlayReadyUnknownOutputPassingOption',
    'ContentKeyPolicyPlayReadyLicenseType',
    'ContentKeyPolicyPlayReadyContentType',
    'ContentKeyPolicyRestrictionTokenType',
    'ContentKeyPolicyFairPlayRentalAndLeaseKeyType',
    'AacAudioProfile',
    'AnalysisResolution',
    'StretchMode',
    'DeinterlaceParity',
    'DeinterlaceMode',
    'Rotation',
    'H264VideoProfile',
    'EntropyMode',
    'H264Complexity',
    'EncoderNamedPreset',
    'InsightsType',
    'OnErrorType',
    'Priority',
    'JobErrorCode',
    'JobErrorCategory',
    'JobRetry',
    'JobState',
    'TrackPropertyType',
    'TrackPropertyCompareOperation',
    'StreamingLocatorContentKeyType',
    'StreamingPolicyStreamingProtocol',
    'EncryptionScheme',
    'LiveOutputResourceState',
    'LiveEventInputProtocol',
    'LiveEventEncodingType',
    'LiveEventResourceState',
    'StreamOptionsFlag',
    'StreamingEndpointResourceState',
]
