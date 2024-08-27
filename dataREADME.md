Data configurations contain the defintion of what resources to create and what data to send. This is done by specifying a heirarchy of Assets, associated resources like Asset Types, and optional stadalone resources that are not tied to the heirarchy.  

## DataConfiguration:

| Parameter                          | Required | Type   | Description                                                                                                  |
| ---------------------------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------ |
|AssetTypes | Optional | [AssetType](#AssetType) List | These are the asset types that are used in the hierarchy|
|Hierarchy |  Optional | [HierarchyNode](#HierarchyNode) | This is the heirachy of assets to create |
|SoloStreamReaders |Optional | [StreamReader](#StreamReader) List   | These are streams not associated with an asset|
|SoloEventReaders |Optional | [EventReader](#EventReader)  List| These are events to include|
|SoloReferenceDataReaders |Optional | [ReferenceDataReader](#ReferenceDataReader)  List  | These are events to include|


### AssetType:
| Parameter                          | Required | Type   | Description                                                                                                  |
| ---------------------------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------ |
|Id | Required | String | AssetType's Id|
|Name |  Optional | String | Name |
|Description |  Optional | String |  |
|Metadata |  Optional | MetadataItem array |  |
|TypeReferences |  Optional | TypeReference array |  |
|Status |  Optional | StatusConfiguration |  |


### HierachyNode:
| Parameter                          | Required | Type   | Description                                                                                                  |
| ---------------------------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------ |
|Asset | Required | [Asset](#Asset) | |
|StreamReaders |  Optional | [StreamReader](#StreamReader) List  | Name |
|EventReader |  Optional | String |  |
|ReferenceDataReader |  Optional | MetadataItem array |  |
|Children |  Optional | [HierarchyNode](#HierarchyNode)  List |  |

note: *uses the hierarchy to create the parent and path metadatas on the asset*

### Asset
| Parameter                          | Required | Type   | Description                                                                                                  |
| ---------------------------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------ |
|Id | Required | String | Asset Id|
|Name |  Optional | String | Name |
|Description |  Optional | String |  |
|StreamReferences |  Optional | [StreamReference](#StreamReference) list | List of properties of the asset |

note: *uses the hierarchy to create the parent and path metadatas on the asset*



### StreamReference:
| Parameter                          | Required | Type   | Description                                                                                                  |
| ---------------------------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------ |
|Id | Required | String | Asset Property Id|
|Name |  Optional | String | Asset Property Name |
|StreamId |  Required | String | Id of the stream |




### StreamReader:
| Parameter                          | Required | Type   | Description                                                                                                  |
| ---------------------------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------ |
|Reader | Required | String | |
|Id | Required | String | Id of the Stream to send data to |
|Name |  Optional | String | Name |
|FilePath |  Required | String |  |
|DataClass |  Required | String |  |



### EventReader:
| Parameter                          | Required | Type   | Description                                                                                                  |
| ---------------------------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------ |
|Reader | Required | String | |
|Id | Required | String | Id|
|Name |  Optional | String | Name |
|FilePath |  Required | String |  |
|EventClass |  Required | String |  |
|AuthorizationTags |  Required | String |  |
|Enumerations |  Required | String |  |
|UnitsOfMeasure |  Required | String |  |
|ReferenceAsset |  Required | String |  |


### ReferenceDataReader:
| Parameter                          | Required | Type   | Description                                                                                                  |
| ---------------------------------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------ |
|Reader | Required | String | |
|Id | Required | String | Id|
|Name |  Optional | String | Name |
|FilePath |  Required | String |  |
|ReferenceDataClass |  Required | String |  |
|ReferenceDataType |  Required | String |  |
|AuthorizationTags |  Required | String |  |
|Enumerations |  Required | String |  |
|UnitsOfMeasure |  Required | String |  |
