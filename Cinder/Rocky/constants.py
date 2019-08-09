# Copyright (c) 2016 Huawei Technologies Co., Ltd.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

STATUS_HEALTH = '1'
LUN_TYPE = '11'
SNAPSHOT_TYPE = '27'
BLOCK_POOL_TYPE = '1'

HOSTGROUP_PREFIX = 'OpenStack_HostGroup_'
LUNGROUP_PREFIX = 'OpenStack_LunGroup_'
MAPPING_VIEW_PREFIX = 'OpenStack_Mapping_View_'
PORTGROUP_PREFIX = 'OpenStack_PortGroup_'
QOS_NAME_PREFIX = 'OpenStack_'

FC_PORT_CONNECTED = '10'
CAPACITY_UNIT = 1024 * 1024 * 2
DEFAULT_WAIT_TIMEOUT = 3600 * 24 * 30
DEFAULT_WAIT_INTERVAL = 5
MAX_NAME_LENGTH = 31
SOCKET_TIMEOUT = 52
LOGIN_SOCKET_TIMEOUT = 4
PWD_EXPIRED_OR_INITIAL = (3, 4)

LUN_STATUS = (LUN_ONLINE, LUN_INITIALIZING, LUN_OFFLINE) = ('27', '53', '28')
SNAPSHOT_STATUS = (
    SNAPSHOT_INITIALIZING, SNAPSHOT_ACTIVATED, SNAPSHOT_UNACTIVATED
) = ('53', '43', '45')

MIGRATION_STATUS_IN_PROCESS = (
    MIGRATION_NORMAL, MIGRATION_QUEUING, MIGRATION_MIGRATING
) = ('1', '37', '75')
MIGRATION_STATUS_COMPLETE = (MIGRATION_COMPLETE,) = ('76',)
LUNCOPY_STATUS_COMPLETE = (LUNCOPY_COMPLETE,) = ('40',)

ERROR_CONNECT_TO_SERVER = -403
ERROR_UNAUTHORIZED_TO_SERVER = -401
OBJECT_NAME_ALREADY_EXIST = 1077948993
OBJECT_ID_NOT_UNIQUE = 1077948997
ERROR_VOLUME_NOT_EXIST = 1077939726
ERROR_LUN_NOT_EXIST = 1077936859
SNAPSHOT_NOT_EXIST = 1077937880
OBJECT_NOT_EXIST = 1077948996
HYPERMETRO_NOT_EXIST = 1077674242
HYPERMETRO_NOT_IN_GROUP = 1077675021
HYPERMETROGROUP_NOT_EXIST = 1077675010
HYPERMETRO_ALREADY_IN_GROUP = 1077675038
NO_HYPERMETRO_EXIST_IN_GROUP = 1077675022
HOSTGROUP_NOT_IN_MAPPINGVIEW = 1073804552
PORTGROUP_NOT_IN_MAPPINGVIEW = 1073804553
LUNGROUP_NOT_IN_MAPPINGVIEW = 1073804554
MIGRATION_NOT_EXIST = 1073806607
LUNCOPY_NOT_EXIST = 50338560
LUNCOPY_ALREADY_STOPPED = 1077950178
LUNCOPY_COMPLETED = 1077950180
PORTGROUP_NOT_EXIST = 1077951832
HOSTGROUP_NOT_EXIST = 1077937500
HOST_NOT_IN_HOSTGROUP = 1073745412
PORT_NOT_IN_PORTGROUP = 1073807618
INITIATOR_NOT_IN_HOST = 1077950342
HOST_NOT_EXIST = 1077937498
MAPPINGVIEW_NOT_EXIST = 1077951819
HOST_ALREADY_IN_HOSTGROUP = 1077937501
PORT_ALREADY_IN_PORTGROUP = 1077951833
HOSTGROUP_ALREADY_IN_MAPPINGVIEW = 1073804556
PORTGROUP_ALREADY_IN_MAPPINGVIEW = 1073804558
LUNGROUP_ALREADY_IN_MAPPINGVIEW = 1073804560

METRO_RUNNING_STATUS = (METRO_RUNNING_NORMAL, METRO_RUNNING_SYNC,
                        METRO_RUNNING_STOP, RUNNING_TO_BE_SYNC
                        ) = ('1', '23', '41', '100')
METRO_HEALTH_NORMAL = '1'

THICK_LUNTYPE = '0'
THIN_LUNTYPE = '1'
LUN_TYPE_MAP = {'Thick': THICK_LUNTYPE,
                'Thin': THIN_LUNTYPE}

QOS_INACTIVATED = '45'
LOWER_LIMIT_KEYS = ('MINIOPS', 'LATENCY', 'MINBANDWIDTH')
UPPER_LIMIT_KEYS = ('MAXIOPS', 'MAXBANDWIDTH')

REPLICA_SYNC_MODEL = '1'
REPLICA_ASYNC_MODEL = '2'
REPLICA_SPEED = '2'
REPLICA_PERIOD = '3600'
REPLICA_SECOND_RO = '2'
REPLICA_SECOND_RW = '3'
REPLICA_CG_PERIOD = '60'

REPLICA_RUNNING_STATUS_SYNC = '23'
REPLICA_RUNNING_STATUS_NORMAL = '1'
REPLICA_RUNNING_STATUS_SPLIT = '26'
REPLICA_RUNNING_STATUS_INTERRUPTED = '34'
REPLICA_SECRES_DATA_SYNC = '1'
REPLICA_SECRES_DATA_COMPLETE = '2'
REPLICA_HEALTH_STATUS_NORMAL = '1'

REPLICATION_PAIR_NOT_EXIST = 1077937923
REPLICATION_GROUP_NOT_EXIST = 1077937924
REPLICATION_PAIR_NOT_GROUP_MEMBER = 1077937927
REPLICATION_GROUP_IS_EMPTY = 1077937960

VALID_PRODUCT = ('V3', 'V5', '18000', 'Dorado')
TIER_DISK_TYPES = ('ssd', 'sas', 'nl_sas')

AVAILABLE_FEATURE_STATUS = (1, 2)
CHECK_FEATURES = {
    'SmartTier': None,
    'SmartThin': None,
    'SmartQoS': 'ioclass',
    'SmartPartition': 'cachepartition',
    'SmartCache': 'smartcachepartition',
    'SmartMigration': 'LUN_MIGRATION',
    'HyperMetro': 'HyperMetroPair',
    'HyperReplication': 'REPLICATIONPAIR',
    'HyperSnap': 'snapshot',
    'HyperCopy': 'LUNCOPY',
    'SmartDedupe[\s\S]*LUN': None,
    'SmartCompression[\s\S]*LUN': None,
}

LUN_COPY_SPEED_TYPES = (
    LUN_COPY_SPEED_LOW,
    LUN_COPY_SPEED_MEDIUM,
    LUN_COPY_SPEED_HIGH,
    LUN_COPY_SPEED_HIGHEST
) = ('1', '2', '3', '4')
DEFAULT_CLONE_MODE = "luncopy"
DEFAULT_WORKLOAD_TYPE_ID = 0
SUPPORT_WORKLOAD_TYPE_VERSION = "V300R001C20"

HYPER_SYNC_SPEED_TYPES = (
    HYPER_SYNC_SPEED_LOW,
    HYPER_SYNC_SPEED_MEDIUM,
    HYPER_SYNC_SPEED_HIGH,
    HYPER_SYNC_SPEED_HIGHEST
) = ('1', '2', '3', '4')

REPLICA_SYNC_SPEED_TYPES = (
    REPLICA_SYNC_SPEED_LOW,
    REPLICA_SYNC_SPEED_MEDIUM,
    REPLICA_SYNC_SPEED_HIGH,
    REPLICA_SYNC_SPEED_HIGHEST
) = ('1', '2', '3', '4')