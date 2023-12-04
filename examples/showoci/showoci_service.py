#########################################################################
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# showoci_service.py
#
# @author: Adi Zohar
# @contributors: Olaf Heimburger
#
# Supports Python 3 and above
#
# coding: utf-8
##########################################################################
# This file has ShowOCIService class, and ShowOCIFlags
#
# ShowOCIService - class has all OCI APIs , once called load_service_data(),
# it will load all the data to the "data" property
#
# ShowOCIFlags   - class has the flags for calling the service Classes
#
# ShowOCIDomains  - class has the identity domain info
#
# PaaS Services - OCE and OIC , ODA Tested
#                 OAC need to be tested
##########################################################################
from __future__ import print_function
import oci
import time
import datetime
import os
import platform
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import threading


##########################################################################
# class ShowOCIService
##########################################################################
class ShowOCIService(object):
    version = "23.11.28"
    oci_compatible_version = "2.110.2"
    thread_lock = threading.Lock()

    ##########################################################################
    # Global Constants
    ##########################################################################

    # print header options
    print_header_options = {0: 90, 1: 60, 2: 40, 3: 75}

    # Network Identifiers
    C_NETWORK = 'network'
    C_NETWORK_IPS = 'ipsec'
    C_NETWORK_VCN = 'vcn'
    C_NETWORK_SGW = 'sgw'
    C_NETWORK_VLAN = 'vlan'
    C_NETWORK_NAT = 'nat'
    C_NETWORK_DRG = 'drg'
    C_NETWORK_CPE = 'cpe'
    C_NETWORK_DRG_AT = 'drg_attached'
    C_NETWORK_DRG_RT = 'drg_route_tables'
    C_NETWORK_RPC = 'rpc'
    C_NETWORK_IGW = 'igw'
    C_NETWORK_LPG = 'lpg'
    C_NETWORK_SLIST = 'seclist'
    C_NETWORK_NSG = 'secgroups'
    C_NETWORK_NSG_REPTEXT = 'NETWORKSECURITYGR'
    C_NETWORK_ROUTE = 'route'
    C_NETWORK_DHCP = 'dhcp'
    C_NETWORK_SUBNET = 'subnet'
    C_NETWORK_SUBNET_PIP = 'private_ips'
    C_NETWORK_VC = 'virtualcircuit'
    C_NETWORK_PRIVATEIP = 'privateip'
    C_NETWORK_DNS_RESOLVERS = 'dns_resolvers'
    C_NETWORK_FIREWALL = 'network_firewall'
    C_NETWORK_FIREWALL_POLICY = 'network_firewall_policy'

    # Identity Identifiers
    C_IDENTITY = 'identity'
    C_IDENTITY_DOMAINS = 'domains'
    C_IDENTITY_ADS = 'availability_domains'
    C_IDENTITY_USERS = 'users'
    C_IDENTITY_GROUPS = 'groups'
    C_IDENTITY_POLICIES = 'policies'
    C_IDENTITY_TAG_NAMESPACE = 'tag_namespace'
    C_IDENTITY_TENANCY = 'tenancy'
    C_IDENTITY_COMPARTMENTS = 'compartments'
    C_IDENTITY_REGIONS = 'regions'
    C_IDENTITY_PROVIDERS = 'providers'
    C_IDENTITY_DYNAMIC_GROUPS = 'dynamic_groups'
    C_IDENTITY_NETWORK_SOURCES = 'network_sources'
    C_IDENTITY_USERS_GROUPS_MEMBERSHIP = 'users_groups_membership'
    C_IDENTITY_COST_TRACKING_TAGS = 'cost_tracking_tags'

    # Compute Identifiers
    C_COMPUTE = 'compute'
    C_COMPUTE_INST = 'instance'
    C_COMPUTE_INST_CONFIG = 'instance_config'
    C_COMPUTE_INST_POOL = 'instance_pool'
    C_COMPUTE_IMAGES = 'instance_image'
    C_COMPUTE_BOOT_VOL_ATTACH = 'instance_boot_vol_attach'
    C_COMPUTE_VOLUME_ATTACH = 'instance_volume_attach'
    C_COMPUTE_VNIC_ATTACH = 'instance_vnic_attach'
    C_COMPUTE_AUTOSCALING = 'auto_scaling'
    C_COMPUTE_CAPACITY_RESERVATION = 'capacity_reservation'

    # Block Storage Identifiers
    C_BLOCK = 'blockstorage'
    C_BLOCK_BOOT = 'boot'
    C_BLOCK_BOOTBACK = 'boot_back'
    C_BLOCK_VOL = 'volume'
    C_BLOCK_VOLBACK = 'volume_back'
    C_BLOCK_VOLGRP = 'volume_group'
    C_BLOCK_VOLGRPBACK = 'volume_group_backup'

    # Load Balancer Identifiers
    C_LB = 'loadbalancer'
    C_LB_LOAD_BALANCERS = 'load_balancers'
    C_LB_BACKEND_SETS = 'backend_sets'
    C_LB_NETWORK_LOAD_BALANCERS = 'network_load_balancers'
    C_LB_NETWORK_BACKEND_SETS = 'network_lb_backend_sets'

    # Load Balancer Identifiers
    C_OS = 'objectstorage'
    C_OS_BUCKETS = 'buckets'

    # Load Balancer Identifiers
    C_ORM = 'resource_management'
    C_ORM_STACKS = 'stacks'

    # Emails
    C_EMAIL = 'email'
    C_EMAIL_SUPPRESSIONS = 'suppressions'
    C_EMAIL_SENDERS = 'senders'

    # File Storage
    C_FILE_STORAGE = 'file_storage'
    C_FILE_STORAGE_FILESYSTEMS = 'filesystems'
    C_FILE_STORAGE_MOUNTS = 'mounts'
    C_FILE_STORAGE_EXPORTS = 'exports'

    # database
    C_DATABASE = "database"
    C_DATABASE_HOMES = "dhomes"
    C_DATABASE_BACKUPS = "backups"
    C_DATABASE_DBSYSTEMS = "dbsystems"
    C_DATABASE_EXADATA = "exadata"
    C_DATABASE_EXADATA_VMS = "exadata_vmclusters"
    C_DATABASE_EXACC_ADB_VMS = "exadata_adb_vmclusters"
    C_DATABASE_EXACC = "exacc"
    C_DATABASE_EXACC_VMS = "exacc_vmclusters"
    C_DATABASE_EXACC_DBSERVERS = "exacc_db_servers"
    C_DATABASE_ADB_DATABASE = "autonomous"
    C_DATABASE_ADB_D_VMS = "autonomous_dedicated_vmclusters"
    C_DATABASE_ADB_D_CONTAINERS = "autonomous_dedicated_containers"
    C_DATABASE_NOSQL = "nosql"
    C_DATABASE_MYSQL = "mysql"
    C_DATABASE_SOFTWARE_IMAGES = "database_software_images"
    C_DATABASE_GG_DEPLOYMENTS = "gg_deployments"
    C_DATABASE_GG_DB_REGISTRATION = "gg_db_registration"
    C_DATABASE_EXTERNAL_CDB = "external_cdb"
    C_DATABASE_EXTERNAL_PDB = "external_pdb"
    C_DATABASE_EXTERNAL_NONPDB = "external_nonpdb"

    # container
    C_CONTAINER = "container"
    C_CONTAINER_CLUSTERS = "clusters"
    C_CONTAINER_NODE_POOLS = "nodepools"

    # streams and queues
    C_STREAMS = "streams_queues"
    C_STREAMS_STREAMS = "streams"
    C_STREAMS_QUEUES = "queues"

    # budgets
    C_BUDGETS = "budgets"
    C_BUDGETS_BUDGETS = "budgets"

    # monitoring
    C_MONITORING = "monitoring"
    C_MONITORING_ALARMS = "alarms"
    C_MONITORING_EVENTS = "events"
    C_MONITORING_AGENTS = "agents"
    C_MONITORING_DB_MANAGEMENT = "db_management"

    # notifications
    C_NOTIFICATIONS = "notifications"
    C_NOTIFICATIONS_TOPICS = "topics"
    C_NOTIFICATIONS_SUBSCRIPTIONS = "subscriptions"

    # edge services and DNS
    C_EDGE = "edge"
    C_EDGE_HEALTHCHECK_PING = "healthcheck_ping"
    C_EDGE_HEALTHCHECK_HTTP = "healthcheck_http"
    C_EDGE_DNS_ZONE = 'dns_zone'
    C_EDGE_DNS_STEERING = 'dns_steering'
    C_EDGE_WAAS_POLICIES = 'waas_policies'
    C_EDGE_WAF = 'waf'

    # Announcement services
    C_ANNOUNCEMENT = "announcement"
    C_ANNOUNCEMENT_ANNOUNCEMENT = "announcements"

    # limits
    C_LIMITS = "limits"
    C_LIMITS_SERVICES = "services"
    C_LIMITS_QUOTAS = "quotas"

    # Native Services
    C_PAAS_NATIVE = "paas_native"
    C_PAAS_NATIVE_OIC = "oic"
    C_PAAS_NATIVE_OAC = "oac"
    C_PAAS_NATIVE_OCE = "oce"
    C_PAAS_NATIVE_OCVS = "ocvs"
    C_PAAS_NATIVE_VB = "vb"
    C_PAAS_NATIVE_DEVOPS = "devops"
    C_PAAS_NATIVE_OPEN_SEARCH = "opensearch"

    # function
    C_FUNCTION = "functions"
    C_FUNCTION_APPLICATIONS = "applications"
    C_FUNCTION_FUNCTIONS = "app_functions"

    # API gateways
    C_API = "apis"
    C_API_GATEWAYS = "gateways"
    C_API_DEPLOYMENT = "deployments"

    # Data and AI
    C_DATA_AI = "data_ai"
    C_DATA_AI_SCIENCE = "data_science"
    C_DATA_AI_CATALOG = "data_catalog"
    C_DATA_AI_DCREGISTRY = "data_connectivity_registry"
    C_DATA_AI_FLOW = "data_flow"
    C_DATA_AI_DI = "data_integration"
    C_DATA_AI_ODA = "oda"
    C_DATA_AI_BDS = "bds"

    # Security and Logging
    C_SECURITY = "security"
    C_SECURITY_CLOUD_GUARD = "cloud_guard"
    C_SECURITY_VAULTS = "vaults"
    C_SECURITY_BASTION = "bastion"
    C_SECURITY_LOGGING = "logging"
    C_SECURITY_LOGGING_UA = "unified_agents"

    # Security Scores
    C_SECURITY_SCORES = "security_scores"
    C_SECURITY_SCORES_GUARD_SECURITY_SCORES = "cloud_guard_security_scores"
    C_SECURITY_SCORES_GUARD_RISK_SCORES = "cloud_guard_risk_scores"

    # Error flag and reboot migration
    error = 0
    warning = 0
    reboot_migration_counter = 0
    dbsystem_maintenance = []
    tenancy_home_region = ""

    ##########################################################################
    # Exclude Services
    ##########################################################################
    EXCLUDE_NETWORK = 'NETWORK'
    EXCLUDE_LIMITS = 'LIMITS'
    EXCLUDE_QUOTAS = 'QUOTAS'
    EXCLUDE_DNSZONE = 'DNSZONE'
    EXCLUDE_VCIRCUITS = 'VCIRCUITS'

    ##########################################################################
    # Service not yet available - need to remove on availability
    ##########################################################################
    service_not_available_array = [
        {'region': 'region_name', 'service': C_EMAIL}
    ]

    ##########################################################################
    # Shapes
    ##########################################################################
    ciphers_array = [
        {'cipher': 'AES128-GCM-SHA256            ', 'tls': 1.2},
        {'cipher': 'AES128-SHA                   ', 'tls': 1.0},
        {'cipher': 'AES128-SHA256                ', 'tls': 1.2},
        {'cipher': 'AES256-GCM-SHA384            ', 'tls': 1.2},
        {'cipher': 'AES256-SHA                   ', 'tls': 1.0},
        {'cipher': 'AES256-SHA256                ', 'tls': 1.2},
        {'cipher': 'CAMELLIA128-SHA              ', 'tls': 1.0},
        {'cipher': 'CAMELLIA256-SHA              ', 'tls': 1.0},
        {'cipher': 'DES-CBC3-SHA                 ', 'tls': 1.0},
        {'cipher': 'DH-DSS-AES128-GCM-SHA256     ', 'tls': 1.2},
        {'cipher': 'DH-DSS-AES128-SHA            ', 'tls': 1.0},
        {'cipher': 'DH-DSS-AES128-SHA256         ', 'tls': 1.2},
        {'cipher': 'DH-DSS-AES256-GCM-SHA384     ', 'tls': 1.2},
        {'cipher': 'DH-DSS-AES256-SHA            ', 'tls': 1.0},
        {'cipher': 'DH-DSS-AES256-SHA256         ', 'tls': 1.2},
        {'cipher': 'DH-DSS-CAMELLIA128-SHA       ', 'tls': 1.0},
        {'cipher': 'DH-DSS-CAMELLIA256-SHA       ', 'tls': 1.0},
        {'cipher': 'DH-DSS-DES-CBC3-SHAv         ', 'tls': 1.0},
        {'cipher': 'DH-DSS-SEED-SHA              ', 'tls': 1.0},
        {'cipher': 'DH-RSA-AES128-GCM-SHA256     ', 'tls': 1.2},
        {'cipher': 'DH-RSA-AES128-SHA            ', 'tls': 1.0},
        {'cipher': 'DH-RSA-AES128-SHA256         ', 'tls': 1.2},
        {'cipher': 'DH-RSA-AES256-GCM-SHA384     ', 'tls': 1.2},
        {'cipher': 'DH-RSA-AES256-SHA            ', 'tls': 1.0},
        {'cipher': 'DH-RSA-AES256-SHA256         ', 'tls': 1.2},
        {'cipher': 'DH-RSA-CAMELLIA128-SHA       ', 'tls': 1.0},
        {'cipher': 'DH-RSA-CAMELLIA256-SHA       ', 'tls': 1.0},
        {'cipher': 'DH-RSA-DES-CBC3-SHA          ', 'tls': 1.0},
        {'cipher': 'DH-RSA-SEED-SHA              ', 'tls': 1.0},
        {'cipher': 'DHE-DSS-AES128-GCM-SHA256    ', 'tls': 1.2},
        {'cipher': 'DHE-DSS-AES128-SHA           ', 'tls': 1.0},
        {'cipher': 'DHE-DSS-AES128-SHA256        ', 'tls': 1.2},
        {'cipher': 'DHE-DSS-AES256-GCM-SHA384    ', 'tls': 1.2},
        {'cipher': 'DHE-DSS-AES256-SHA           ', 'tls': 1.0},
        {'cipher': 'DHE-DSS-AES256-SHA256        ', 'tls': 1.2},
        {'cipher': 'DHE-DSS-CAMELLIA128-SHA      ', 'tls': 1.0},
        {'cipher': 'DHE-DSS-CAMELLIA256-SHA      ', 'tls': 1.0},
        {'cipher': 'DHE-DSS-DES-CBC3-SHA         ', 'tls': 1.0},
        {'cipher': 'DHE-DSS-SEED-SHA             ', 'tls': 1.0},
        {'cipher': 'DHE-RSA-AES128-GCM-SHA256    ', 'tls': 1.2},
        {'cipher': 'DHE-RSA-AES128-SHA           ', 'tls': 1.0},
        {'cipher': 'DHE-RSA-AES128-SHA256        ', 'tls': 1.2},
        {'cipher': 'DHE-RSA-AES256-GCM-SHA384    ', 'tls': 1.2},
        {'cipher': 'DHE-RSA-AES256-SHA           ', 'tls': 1.0},
        {'cipher': 'DHE-RSA-AES256-SHA256        ', 'tls': 1.2},
        {'cipher': 'DHE-RSA-CAMELLIA128-SHA      ', 'tls': 1.0},
        {'cipher': 'DHE-RSA-CAMELLIA256-SHA      ', 'tls': 1.0},
        {'cipher': 'DHE-RSA-DES-CBC3-SHA         ', 'tls': 1.0},
        {'cipher': 'DHE-RSA-SEED-SHA             ', 'tls': 1.0},
        {'cipher': 'ECDH-ECDSA-AES128-GCM-SHA256 ', 'tls': 1.2},
        {'cipher': 'ECDH-ECDSA-AES128-SHA        ', 'tls': 1.0},
        {'cipher': 'ECDH-ECDSA-AES128-SHA256     ', 'tls': 1.2},
        {'cipher': 'ECDH-ECDSA-AES256-GCM-SHA384 ', 'tls': 1.2},
        {'cipher': 'ECDH-ECDSA-AES256-SHA        ', 'tls': 1.0},
        {'cipher': 'ECDH-ECDSA-AES256-SHA384     ', 'tls': 1.2},
        {'cipher': 'ECDH-ECDSA-DES-CBC3-SHA      ', 'tls': 1.0},
        {'cipher': 'ECDH-ECDSA-RC4-SHA           ', 'tls': 1.0},
        {'cipher': 'ECDH-RSA-AES128-GCM-SHA256   ', 'tls': 1.2},
        {'cipher': 'ECDH-RSA-AES128-SHA          ', 'tls': 1.0},
        {'cipher': 'ECDH-RSA-AES128-SHA256       ', 'tls': 1.2},
        {'cipher': 'ECDH-RSA-AES256-GCM-SHA384   ', 'tls': 1.2},
        {'cipher': 'ECDH-RSA-AES256-SHA          ', 'tls': 1.0},
        {'cipher': 'ECDH-RSA-AES256-SHA384       ', 'tls': 1.2},
        {'cipher': 'ECDH-RSA-DES-CBC3-SHA        ', 'tls': 1.0},
        {'cipher': 'ECDH-RSA-RC4-SHA             ', 'tls': 1.0},
        {'cipher': 'ECDHE-ECDSA-AES128-GCM-SHA256', 'tls': 1.2},
        {'cipher': 'ECDHE-ECDSA-AES128-SHA       ', 'tls': 1.0},
        {'cipher': 'ECDHE-ECDSA-AES128-SHA256    ', 'tls': 1.2},
        {'cipher': 'ECDHE-ECDSA-AES256-GCM-SHA384', 'tls': 1.2},
        {'cipher': 'ECDHE-ECDSA-AES256-SHA       ', 'tls': 1.0},
        {'cipher': 'ECDHE-ECDSA-AES256-SHA384    ', 'tls': 1.2},
        {'cipher': 'ECDHE-ECDSA-DES-CBC3-SHA     ', 'tls': 1.1},
        {'cipher': 'ECDHE-ECDSA-RC4-SHA          ', 'tls': 1.0},
        {'cipher': 'ECDHE-RSA-AES128-GCM-SHA256  ', 'tls': 1.2},
        {'cipher': 'ECDHE-RSA-AES128-SHA         ', 'tls': 1.0},
        {'cipher': 'ECDHE-RSA-AES128-SHA256      ', 'tls': 1.2},
        {'cipher': 'ECDHE-RSA-AES256-GCM-SHA384  ', 'tls': 1.2},
        {'cipher': 'ECDHE-RSA-AES256-SHA         ', 'tls': 1.0},
        {'cipher': 'ECDHE-RSA-AES256-SHA384      ', 'tls': 1.2},
        {'cipher': 'ECDHE-RSA-DES-CBC3-SHA       ', 'tls': 1.0},
        {'cipher': 'ECDHE-RSA-RC4-SHA            ', 'tls': 1.0},
        {'cipher': 'IDEA-CBC-SHA                 ', 'tls': 1.0},
        {'cipher': 'KRB5-DES-CBC3-MD5            ', 'tls': 1.0},
        {'cipher': 'KRB5-DES-CBC3-SHA            ', 'tls': 1.0},
        {'cipher': 'KRB5-IDEA-CBC-MD5            ', 'tls': 1.0},
        {'cipher': 'KRB5-IDEA-CBC-SHA            ', 'tls': 1.0},
        {'cipher': 'KRB5-RC4-MD5                 ', 'tls': 1.0},
        {'cipher': 'KRB5-RC4-SHA                 ', 'tls': 1.0},
        {'cipher': 'PSK-3DES-EDE-CBC-SHA         ', 'tls': 1.0},
        {'cipher': 'PSK-AES128-CBC-SHA           ', 'tls': 1.0},
        {'cipher': 'PSK-AES256-CBC-SHA           ', 'tls': 1.0},
        {'cipher': 'PSK-RC4-SHA                  ', 'tls': 1.0},
        {'cipher': 'RC4-MD5                      ', 'tls': 1.0},
        {'cipher': 'RC4-SHA                      ', 'tls': 1.0},
        {'cipher': 'SEED-SHA                     ', 'tls': 1.0}]

    ##########################################################################
    # Shapes
    ##########################################################################
    shapes_array = [
        {'shape': 'BM.CPU3.8', 'cpu': 52, 'memory': 768, 'storage': 0},
        {'shape': 'BM.DenseIO1.36', 'cpu': 36, 'memory': 512, 'storage': 28.8},
        {'shape': 'BM.DenseIO2.52', 'cpu': 52, 'memory': 768, 'storage': 51.2},
        {'shape': 'BM.GPU2.2', 'cpu': 28, 'memory': 192, 'storage': 0},
        {'shape': 'BM.HPC2.36', 'cpu': 36, 'memory': 384, 'storage': 0},
        {'shape': 'BM.HighIO1.36', 'cpu': 36, 'memory': 512, 'storage': 12.8},
        {'shape': 'BM.RACLocalStorage1.72', 'cpu': 72, 'memory': 1024, 'storage': 64},
        {'shape': 'BM.Standard1.36', 'cpu': 36, 'memory': 256, 'storage': 0},
        {'shape': 'BM.Standard2.52', 'cpu': 52, 'memory': 768, 'storage': 0},
        {'shape': 'BM.StandardE2.64', 'cpu': 64, 'memory': 512, 'storage': 0},
        {'shape': 'BM.Standard.B1.44', 'cpu': 44, 'memory': 512, 'storage': 0},
        {'shape': 'BM.Standard.E2.64', 'cpu': 64, 'memory': 512, 'storage': 0},
        {'shape': 'Exadata.Full1.336', 'cpu': 336, 'memory': 5760, 'storage': 336},
        {'shape': 'Exadata.Half1.168', 'cpu': 168, 'memory': 2880, 'storage': 168},
        {'shape': 'Exadata.Quarter1.84', 'cpu': 84, 'memory': 1440, 'storage': 84},
        {'shape': 'Exadata.Full2.368', 'cpu': 368, 'memory': 5760, 'storage': 424},
        {'shape': 'Exadata.Half2.184', 'cpu': 184, 'memory': 2880, 'storage': 212},
        {'shape': 'Exadata.Quarter2.92', 'cpu': 92, 'memory': 1440, 'storage': 106},
        {'shape': 'Exadata.Full3.400', 'cpu': 400, 'memory': 5760, 'storage': 598},
        {'shape': 'Exadata.Half3.200', 'cpu': 200, 'memory': 2880, 'storage': 298},
        {'shape': 'Exadata.Quarter3.100', 'cpu': 100, 'memory': 1440, 'storage': 149},
        {'shape': 'Exadata.X8M', 'cpu': 100, 'memory': 1440, 'storage': 149},
        {'shape': 'Exadata.Base.48', 'cpu': 48, 'memory': 720, 'storage': 74.8},
        {'shape': 'VM.CPU3.1', 'cpu': 6, 'memory': 90, 'storage': 0},
        {'shape': 'VM.CPU3.2', 'cpu': 12, 'memory': 180, 'storage': 0},
        {'shape': 'VM.CPU3.4', 'cpu': 24, 'memory': 360, 'storage': 0},
        {'shape': 'VM.DenseIO1.16', 'cpu': 16, 'memory': 240, 'storage': 12.8},
        {'shape': 'VM.DenseIO1.4', 'cpu': 4, 'memory': 60, 'storage': 3.2},
        {'shape': 'VM.DenseIO1.8', 'cpu': 8, 'memory': 120, 'storage': 6.4},
        {'shape': 'VM.DenseIO2.16', 'cpu': 16, 'memory': 240, 'storage': 12.8},
        {'shape': 'VM.DenseIO2.24', 'cpu': 24, 'memory': 320, 'storage': 25.6},
        {'shape': 'VM.DenseIO2.8', 'cpu': 8, 'memory': 120, 'storage': 6.4},
        {'shape': 'VM.GPU2.1', 'cpu': 12, 'memory': 104, 'storage': 0},
        {'shape': 'VM.Standard.E2.1.Micro', 'cpu': 1, 'memory': 1, 'storage': 0},
        {'shape': 'VM.Standard.E2.1', 'cpu': 1, 'memory': 8, 'storage': 0},
        {'shape': 'VM.Standard.E2.2', 'cpu': 2, 'memory': 16, 'storage': 0},
        {'shape': 'VM.Standard.E2.4', 'cpu': 4, 'memory': 32, 'storage': 0},
        {'shape': 'VM.Standard.E2.8', 'cpu': 8, 'memory': 64, 'storage': 0},
        {'shape': 'VM.Standard1.1', 'cpu': 1, 'memory': 7, 'storage': 0},
        {'shape': 'VM.Standard1.2', 'cpu': 2, 'memory': 14, 'storage': 0},
        {'shape': 'VM.Standard1.4', 'cpu': 4, 'memory': 28, 'storage': 0},
        {'shape': 'VM.Standard1.8', 'cpu': 8, 'memory': 56, 'storage': 0},
        {'shape': 'VM.Standard1.16', 'cpu': 16, 'memory': 112, 'storage': 0},
        {'shape': 'VM.Standard.B1.1', 'cpu': 1, 'memory': 12, 'storage': 0},
        {'shape': 'VM.Standard.B1.2', 'cpu': 2, 'memory': 24, 'storage': 0},
        {'shape': 'VM.Standard.B1.4', 'cpu': 4, 'memory': 48, 'storage': 0},
        {'shape': 'VM.Standard.B1.8', 'cpu': 8, 'memory': 96, 'storage': 0},
        {'shape': 'VM.Standard.B1.16', 'cpu': 16, 'memory': 192, 'storage': 0},
        {'shape': 'VM.Standard2.1', 'cpu': 1, 'memory': 15, 'storage': 0},
        {'shape': 'VM.Standard2.2', 'cpu': 2, 'memory': 30, 'storage': 0},
        {'shape': 'VM.Standard2.4', 'cpu': 4, 'memory': 60, 'storage': 0},
        {'shape': 'VM.Standard2.8', 'cpu': 8, 'memory': 120, 'storage': 0},
        {'shape': 'VM.Standard2.16', 'cpu': 16, 'memory': 240, 'storage': 0},
        {'shape': 'VM.Standard2.24', 'cpu': 24, 'memory': 320, 'storage': 0}
    ]

    ##########################################################################
    # Database Version Date
    ##########################################################################
    database_version_array = [
        {'date': '2019-04', 'version': '18.6'},
        {'date': '2019-07', 'version': '18.7'},
        {'date': '2019-10', 'version': '18.8'},
        {'date': '2020-01', 'version': '18.9'},
        {'date': '2020-04', 'version': '18.10'},
        {'date': '2020-07', 'version': '18.11'},
        {'date': '2020-10', 'version': '18.12'},
        {'date': '2021-01', 'version': '18.13'},
        {'date': '2021-04', 'version': '18.14'},
        {'date': '2021-07', 'version': '18.15'},
        {'date': '2021-10', 'version': '18.16'},
        {'date': '2022-01', 'version': '18.17'},
        {'date': '2022-04', 'version': '18.18'},
        {'date': '2022-07', 'version': '18.19'},
        {'date': '2022-10', 'version': '18.20'},
        {'date': '2023-01', 'version': '18.21'},
        {'date': '2023-04', 'version': '18.22'},
        {'date': '2023-07', 'version': '18.23'},
        {'date': '2023-10', 'version': '18.24'},
        {'date': '2021-01', 'version': '19.6'},
        {'date': '2021-04', 'version': '19.7'},
        {'date': '2021-07', 'version': '19.8'},
        {'date': '2020-10', 'version': '19.9'},
        {'date': '2021-01', 'version': '19.10'},
        {'date': '2021-04', 'version': '19.11'},
        {'date': '2021-07', 'version': '19.12'},
        {'date': '2021-10', 'version': '19.13'},
        {'date': '2022-01', 'version': '19.14'},
        {'date': '2022-04', 'version': '19.15'},
        {'date': '2022-07', 'version': '19.16'},
        {'date': '2022-10', 'version': '19.17'},
        {'date': '2023-01', 'version': '19.18'},
        {'date': '2023-04', 'version': '19.19'},
        {'date': '2023-07', 'version': '19.20'},
        {'date': '2023-10', 'version': '19.21'},
        {'date': '2020-12', 'version': '21.1'},
        {'date': '2021-04', 'version': '21.2'},
        {'date': '2021-07', 'version': '21.3'},
        {'date': '2021-10', 'version': '21.4'},
        {'date': '2022-01', 'version': '21.5'},
        {'date': '2022-04', 'version': '21.6'},
        {'date': '2022-07', 'version': '21.7'},
        {'date': '2022-10', 'version': '21.8'},
        {'date': '2023-01', 'version': '21.9'},
        {'date': '2023-04', 'version': '21.10'},
        {'date': '2023-07', 'version': '21.11'},
        {'date': '2023-10', 'version': '21.12'},
    ]

    ##########################################################################
    # Local Variables
    # data - hold the data data
    # flags - hold the extract flags
    ##########################################################################
    flags = None
    data = {}

    ##########################################################################
    # init class
    # Creates a new data object
    #
    # required:
    #    flags parameters - Class ShowOCIFlags
    #
    ##########################################################################
    def __init__(self, flags):

        # Initiate data everytime class is instantiated
        self.data = {}

        if not isinstance(flags, ShowOCIFlags):
            raise TypeError("flags must be ShowOCIFlags class")

        # check OCI Compatible
        self.check_oci_version_compatible()

        # assign the flags variable
        self.flags = flags

        # if intance pricipals - generate signer from token or config
        if flags.use_instance_principals:
            self.generate_signer_from_instance_principals()

        # if resource pricipals - generate signer from token or config
        elif flags.use_resource_principals:
            self.generate_signer_from_resource_principals()

        # if delegation token for cloud shell
        elif flags.use_delegation_token:
            self.generate_signer_from_delegation_token()

        # if security token and config
        elif flags.use_security_token:
            self.generate_signer_from_config_and_security_token(flags.config_file, flags.config_section)

        # else use config file
        else:
            self.generate_signer_from_config(flags.config_file, flags.config_section)

    ##########################################################################
    # Generate Signer from config
    ###########################################################################
    def generate_signer_from_config(self, config_file, config_section):

        try:
            # create signer from config for authentication
            self.config = oci.config.from_file(config_file, config_section)
            self.signer = oci.signer.Signer(
                tenancy=self.config["tenancy"],
                user=self.config["user"],
                fingerprint=self.config["fingerprint"],
                private_key_file_location=self.config.get("key_file"),
                pass_phrase=oci.config.get_config_value_or_default(self.config, "pass_phrase"),
                private_key_content=self.config.get("key_content")
            )
        except oci.exceptions.ProfileNotFound as e:
            print("*********************************************************************")
            print("* " + str(e))
            print("* Aborting.                                                         *")
            print("*********************************************************************")
            print("")
            raise SystemExit

    ##########################################################################
    # Generate Signer from config and security token
    ###########################################################################
    def generate_signer_from_config_and_security_token(self, config_file, config_section):

        try:
            # create signer from config and security token
            self.config = oci.config.from_file(config_file, config_section)
            security_token_file = self.config.get("security_token_file")
            token = None
            with open(security_token_file, 'r') as f:
                token = f.read()
            private_key = oci.signer.load_private_key_from_file(self.config['key_file'])
            self.signer = oci.auth.signers.SecurityTokenSigner(token, private_key)

        except oci.exceptions.ProfileNotFound as e:
            print("*********************************************************************")
            print("* " + str(e))
            print("* Aborting.                                                         *")
            print("*********************************************************************")
            print("")
            raise SystemExit

        except Exception as e:
            print("*********************************************************************")
            print("* " + str(e))
            print("* Aborting.                                                         *")
            print("*********************************************************************")
            print("")
            raise SystemExit

    ##########################################################################
    # Generate Signer from instance_principals
    ###########################################################################
    def generate_signer_from_instance_principals(self):

        try:
            # get signer from instance principals token
            self.signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

        except Exception:
            print("*********************************************************************")
            print("* Error obtaining instance principals certificate.                  *")
            print("* Aborting.                                                         *")
            print("*********************************************************************")
            print("")
            raise SystemExit

        # generate config info from signer
        self.config = {'region': self.signer.region, 'tenancy': self.signer.tenancy_id}

    ##########################################################################
    # Generate Signer from resource_principals
    ###########################################################################
    def generate_signer_from_resource_principals(self):

        try:
            # get signer from instance principals token
            self.signer = oci.auth.signers.get_resource_principals_signer()

        except Exception:
            print("*********************************************************************")
            print("* Error obtaining resource principals certificate.                  *")
            print("* Aborting.                                                         *")
            print("*********************************************************************")
            print("")
            raise SystemExit

        # generate config info from signer
        self.config = {'region': self.signer.region, 'tenancy': self.signer.tenancy_id}

    ##########################################################################
    # Generate Signer from delegation_token
    # use host variable to point to the OCI Config file and profile
    ###########################################################################
    def generate_signer_from_delegation_token(self):

        # check if env variables OCI_CONFIG_FILE, OCI_CONFIG_PROFILE exist and use them
        env_config_file = os.environ.get('OCI_CONFIG_FILE')
        env_config_section = os.environ.get('OCI_CONFIG_PROFILE')

        # check if file exist
        if env_config_file is not None and env_config_section is not None:
            if os.path.isfile(env_config_file):
                self.flags.config_file = env_config_file
                self.flags.config_section = env_config_section

        try:
            self.config = oci.config.from_file(self.flags.config_file, self.flags.config_section)
            delegation_token_location = self.config["delegation_token_file"]

            with open(delegation_token_location, 'r') as delegation_token_file:
                delegation_token = delegation_token_file.read().strip()
                # get signer from delegation token
                self.signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(delegation_token=delegation_token)

        except KeyError:
            print("*********************************************************************")
            print("* Key Error obtaining delegation_token_file")
            print("* Config  File = " + self.flags.config_file)
            print("* Section File = " + self.flags.config_section)
            print("* Aborting.                                                         *")
            print("*********************************************************************")
            print("")
            raise SystemExit

        except Exception:
            print("*********************************************************************")
            print("* Error obtaining instance principals certificate                   *")
            print("* with delegation token                                             *")
            print("* Aborting.                                                         *")
            print("*********************************************************************")
            print("")
            raise SystemExit

        # generate config info from signer
        tenancy_id = self.config["tenancy"]
        self.config = {'region': self.signer.region, 'tenancy': tenancy_id}

    ##########################################################################
    # load_data
    ##########################################################################
    def load_service_data(self):
        return self.__load_data_main()

    ##########################################################################
    # Print header centered
    ##########################################################################
    def print_header(self, name, category):
        chars = int(self.print_header_options[category])
        print("")
        print('#' * chars)
        print("#" + str(name).center(chars - 2, " ") + "#")
        print('#' * chars)

    ##########################################################################
    # return tenancy data
    ##########################################################################
    def get_tenancy(self):
        return self.data[self.C_IDENTITY][self.C_IDENTITY_TENANCY]

    ##########################################################################
    # get value from service
    ##########################################################################
    def get_value(self, in_value):
        try:
            out_value = ""
            if in_value:
                if str(in_value).lower() == "false" or str(in_value).lower() == "true":
                    out_value = str(in_value).capitalize()
                elif str(in_value).lower() == "none":
                    out_value = ""
                else:
                    out_value = str(in_value)
            return out_value

        except Exception as e:
            self.__print_error("get_value", e)

    ##########################################################################
    # get tenancy id from file or override
    ##########################################################################
    def get_tenancy_id(self):
        if self.flags.filter_by_tenancy_id:
            return self.flags.filter_by_tenancy_id
        else:
            return self.config["tenancy"]

    ##########################################################################
    # return compartment data
    ##########################################################################
    def get_compartment(self):
        return self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS]

    ##########################################################################
    # return compartment by id
    ##########################################################################
    def get_compartment_by_id(self, compartment_id):
        try:
            compartments = self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS]
            for c in compartments:
                if c['id'] == compartment_id:
                    return c
            return {}
        except Exception as e:
            self.__print_error("get_compartment_by_id", e)

    ##########################################################################
    # return availability domains
    ##########################################################################
    def get_availability_domains(self, region_name):
        ads = self.data[self.C_IDENTITY][self.C_IDENTITY_ADS]
        return [e for e in ads if e['region_name'] == region_name]

    ##########################################################################
    # return budget data
    ##########################################################################
    def get_budgets(self):
        if self.C_BUDGETS in self.data:
            if self.C_BUDGETS_BUDGETS in self.data[self.C_BUDGETS]:
                return self.data[self.C_BUDGETS][self.C_BUDGETS_BUDGETS]
        return []

    ##########################################################################
    # return certificate info for load balancer
    ##########################################################################
    def __get_certificate_info(self, cert_array):

        val = ""
        try:
            if cert_array:
                # loop on certificates and extract ca and public
                for key in cert_array.keys():
                    if cert_array[key]:
                        cert = cert_array[key]
                        val += ("," if val else "") + key + "=" + ('ca_certificate' if cert.ca_certificate else "") + (":" if cert.ca_certificate and cert.public_certificate else "") + ("public_certificate" if cert.public_certificate else "")

            return val

        except Exception as e:
            self.__print_error("__get_certificate_info", e)

    ##########################################################################
    # return announcement data
    ##########################################################################
    def get_announcement(self):
        if self.C_ANNOUNCEMENT in self.data:
            if self.C_ANNOUNCEMENT_ANNOUNCEMENT in self.data[self.C_ANNOUNCEMENT]:
                return self.data[self.C_ANNOUNCEMENT][self.C_ANNOUNCEMENT_ANNOUNCEMENT]
        return []

    ##########################################################################
    # return security scores
    ##########################################################################
    def get_security_scores(self):
        if self.C_SECURITY_SCORES in self.data:
            return self.data[self.C_SECURITY_SCORES]
        return []

    ##########################################################################
    # return log by resource
    ##########################################################################
    def get_logging_log(self, resource_id):
        data = []
        try:

            if self.C_SECURITY not in self.data:
                return data
            if self.C_SECURITY_LOGGING not in self.data[self.C_SECURITY]:
                return data

            array = self.data[self.C_SECURITY][self.C_SECURITY_LOGGING]
            for item in array:
                if 'logs' in item:
                    for log in item['logs']:
                        if 'source_resource' in log and 'lifecycle_state' in log:
                            if log['source_resource'] == resource_id and log['lifecycle_state'] == 'ACTIVE':
                                data.append(log)
            return data

        except Exception as e:
            self.__print_error("get_logging_log", e)

    ##########################################################################
    # return subnet
    ##########################################################################
    def get_network_subnet(self, subnet_id, detailed=False):
        try:
            result = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_SUBNET, 'id', subnet_id)
            if result:
                if result != "":
                    if detailed:
                        return result['name'] + ",  " + result['cidr_block'] + ", VCN (" + result['vcn_name'] + ")"
                    else:
                        return result['name']
            return ""

        except Exception as e:
            self.__print_error("get_network_subnet", e)

    ##########################################################################
    # return vcn
    ##########################################################################
    def get_network_vcn(self, vcn_id):
        try:
            result = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_VCN, 'id', vcn_id)
            if result:
                if result != "":
                    return result['name']
            return ""

        except Exception as e:
            self.__print_error("get_network_vcn", e)

    ##########################################################################
    # get_network_drg_route_table
    ##########################################################################
    def get_network_drg_route_table(self, drg_route_table_id):
        try:
            route = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_DRG_RT, 'id', drg_route_table_id)
            if route:
                if 'display_name' in route:
                    return route['display_name']
            return ""

        except Exception as e:
            self.__print_error("get_network_drg_route_table", e)

    ##########################################################################
    # return identity data
    ##########################################################################
    def get_identity(self):
        return self.data[self.C_IDENTITY]

    ##########################################################################
    # return oci version
    ##########################################################################
    def get_oci_version(self):
        return oci.version.__version__

    ##########################################################################
    # check if service available (if not exist in the array then available
    ##########################################################################
    def check_if_service_available(self, region_name, service_name):
        for array in self.service_not_available_array:
            if array['region'] == region_name and array['service'] == service_name:
                return False
        return True

    ##########################################################################
    # check_lifecycle_state_not_terminated
    ##########################################################################
    def check_lifecycle_state_active(self, lifecycle_state):
        return not (lifecycle_state == 'DELETED' or lifecycle_state == 'DELETING' or
                    lifecycle_state == 'TERMINATED' or lifecycle_state == 'TERMINATING' or
                    lifecycle_state == 'UNAVAILABLE' or
                    lifecycle_state == 'MIGRATED')

    ##########################################################################
    # find shape info
    # returns CPUs, Memory and Local Storage SSD
    ##########################################################################
    def get_shape_details(self, shape_name):
        for array in self.shapes_array:
            if array['shape'] == shape_name:
                return array
        return {}

    ##########################################################################
    # find cipher info
    # returns tls
    ##########################################################################
    def get_cipher_tls(self, cipher_name):
        for array in self.ciphers_array:
            if str(array['cipher']).strip() == cipher_name:
                return str(array['tls'])
        return ""

    ##########################################################################
    # find database version date
    ##########################################################################
    def get_database_gi_version_date(self, gi_version):
        if not gi_version:
            return ""

        # split gi to array
        valarr = gi_version.split(".")
        if len(valarr) < 2:
            return ""

        # get onlh 2 left positions
        val = valarr[0] + "." + valarr[1]

        for array in self.database_version_array:
            if array['version'] == val:
                return array['date']

        return ""

    ##########################################################################
    # find database system date
    ##########################################################################
    def get_database_system_version_date(self, system_version):
        if not system_version:
            return ""

        # split gi to array
        for val in system_version.split("."):
            if len(val) == 6:
                return "20" + val[0:2] + "-" + val[2:4]
        return ""

    ##########################################################################
    # Get Database Edition
    ##########################################################################
    def get_database_short_edition(self, edition):
        if not edition:
            return ""

        if edition == "ENTERPRISE_EDITION":
            return "EE"
        elif edition == "ENTERPRISE_EDITION_EXTREME_PERFORMANCE":
            return "XP"
        elif edition == "ENTERPRISE_EDITION_HIGH_PERFORMANCE":
            return "HP"
        elif edition == "STANDARD_EDITION":
            return "SE"
        else:
            return edition

    ##########################################################################
    # Get Database Short license
    ##########################################################################
    def get_database_short_license(self, license):
        if not license:
            return ""

        if license == "BRING_YOUR_OWN_LICENSE":
            return "BYOL"
        elif license == "LICENSE_INCLUDED":
            return "INCL"
        else:
            return license

    ##########################################################################
    # check oci version
    ##########################################################################
    def check_oci_version_compatible(self):

        try:
            # loop on digits
            for i, rl in zip(self.get_oci_version().split("."), self.oci_compatible_version.split(".")):
                if int(i) > int(rl):
                    return True
                if int(i) < int(rl):
                    print("")
                    print("*********************************************************************")
                    print("Error, OCI SDK minimum version " + self.oci_compatible_version + " required !")
                    print("OCI SDK Version installed = " + self.get_oci_version())
                    print("Please use below command to upgrade OCI SDK:")
                    print("   python -m pip install --upgrade oci")
                    print("")
                    print("Aborting.")
                    print("*********************************************************************")
                    print("")
                    raise SystemExit

        except Exception as e:
            self.__print_error("check_oci_version_compatible", e)

    ##########################################################################
    # search unique items with multi parameters
    # parameters are
    # MODULE - data Module
    # SECTION - data Sub module
    # P1, v1 - param and value
    # p2, v2 - param and value - optional
    # p3, v3 - param and value - optional
    ##########################################################################

    def search_unique_item(self, module, section, p1, v1, p2=None, v2=None, p3=None, v3=None):
        try:
            result = self.search_multi_items(module, section, p1, v1, p2, v2, p3, v3)

            if not result:
                return None

            return result[0]

        except Exception as e:
            self.__print_error("search_unique_item", e)

    ##########################################################################
    # search multi items with multi parameters
    # parameters are
    # MODULE - data Module
    # SECTION - data Sub module
    # P1, v1 - param and value
    # p2, v2 - param and value - optional
    # p3, v3 - param and value - optional
    ##########################################################################

    def search_multi_items(self, module, section, p1, v1, p2=None, v2=None, p3=None, v3=None):
        try:
            if len(module) == 0 or len(section) == 0:
                return []

            # check if module exists
            if module not in self.data:
                return []

            # check if section exists
            if section not in self.data[module]:
                return []

            # assign data area to array
            array = self.data[module][section]

            # check parameters and search
            if p2 and v2 and p3 and v3:
                return [e for e in array if e[p1] == v1 and e[p2] == v2 and e[p3] == v3]

            # check parameters and search
            if p2 and v2:
                return [e for e in array if e[p1] == v1 and e[p2] == v2]

            return [e for e in array if e[p1] == v1]

        except Exception as e:
            self.__print_error("search_multi_items " + module + ":" + section, e)

    ##########################################################################
    # initialize data key if not exist
    ##########################################################################
    def __initialize_data_key(self, module, section):
        if module not in self.data:
            self.data[module] = {}
        if section not in self.data[module]:
            self.data[module][section] = []

    ##########################################################################
    # print status message with Threads
    ##########################################################################
    def __load_print_status_with_threads(self, msg):
        if self.flags.skip_threads:
            print("--> " + msg.ljust(32) + "<-- ", end="")
        # else:
            # print("=== Running " + msg + "...")

    ##########################################################################
    # Print Section Time
    ##########################################################################
    def __load_print_section_time(self, section_start_time):
        et = time.time() - section_start_time
        print("Section Elapsed Time " + '{:02d}:{:02d}:{:02d}'.format(round(et // 3600), (round(et % 3600 // 60)), round(et % 60)))

    ##########################################################################
    # print print error
    ##########################################################################
    def __print_error(self, msg, e, compartment=[]):

        try:
            classname = type(self).__name__
            compartment_info = ""

            if compartment:
                if 'name' in compartment:
                    compartment_info = " in compartment " + compartment['name']

            if 'TooManyRequests' in str(e):
                print(" - TooManyRequests Err in " + msg + compartment_info)
            elif isinstance(e, KeyError):
                print("\nError in " + classname + ":" + msg + ": KeyError " + str(e.args) + compartment_info)
            else:
                print("\nError in " + classname + ":" + msg + ": " + str(e) + compartment_info)

            self.error += 1

        except Exception as e:
            print("\nError in __print_error " + str(e))

    ##########################################################################
    # check service error to warn instead of error
    ##########################################################################
    def __check_service_error(self, code):
        return ('remote end closed' in str(code).lower() or
                'max retries exceeded' in str(code).lower() or
                'auth' in str(code).lower() or
                'aborted' in str(code).lower() or
                'notfound' in str(code).lower() or
                'closed connection' in str(code).lower() or
                code == 'Forbidden' or
                code == 'KmsKeyDisabled' or
                code == 'TooManyRequests' or
                code == 'NotAuthorizedOrNotFound' or
                code == 'IncorrectState' or
                code == 'LimitExceeded'
                )

    ##########################################################################
    # check request error if service not exists for region
    ##########################################################################
    def __check_request_error(self, e):

        # service not yet available
        if (
                ('Errno 8' in str(e) and 'NewConnectionError' in str(e)) or
                'Max retries exceeded' in str(e) or
                'HTTPSConnectionPool' in str(e) or
                'not currently available' in str(e) or
                'closed connection' in str(e)
        ):
            print("Service Not Accessible or not yet exist")
            return True

        # if ReadTimeoutError timeout
        if ('ReadTimeoutError' in str(e)):
            print("ReadTimeoutError, Please use higher value with -readtimeout flag !\nError: " + str(e))
            self.error += 1
            return True

        # if Connection TimeoutError timeout
        if ('TimeoutError' in str(e)):
            print("Connection TimeoutError, Please use higher value with -conntimeout flag !\nError: " + str(e))
            self.error += 1
            return True

        return False

    ##########################################################################
    # check if managed paas compartment
    ##########################################################################
    def __if_managed_paas_compartment(self, name):
        return name == "ManagedCompartmentForPaaS"

    ##########################################################################
    # print count result for Thread
    ##########################################################################
    def __load_print_thread_cnt(self, header, cnt, start_time, errstr):

        et = time.time() - start_time
        str_time = '{:02d}:{:02d}:{:02d}'.format(round(et // 3600), (round(et % 3600 // 60)), round(et % 60))
        str_cnt = str("(" + str(cnt) + ")").ljust(7)

        if self.flags.skip_threads:
            print(" " + str_cnt + " - " + str_time)
        else:
            # lock for printing
            with self.thread_lock:
                str1 = "--> " + header.ljust(32) + "<-- "
                str2 = str_cnt + " - " + str_time + ((" - " + errstr) if errstr else "")
                print(str1 + str2)

    ##########################################################################
    # print auth warning
    ##########################################################################
    def __load_print_auth_warning(self, special_char="a", increase_warning=True, to_print=True):
        if increase_warning:
            self.warning += 1
        if to_print:
            print(special_char, end="")

    ##########################################################################
    # Main procedure to read data to the data
    ##########################################################################
    def __load_data_main(self):
        try:
            print("Guide: '.' Compartment, '+' VCN, '-' Subnets, 'a' - auth/notfound")

            # print filter by
            if self.flags.filter_by_region:
                print("Filtered by Regions       = " + self.flags.filter_by_region)

            if self.flags.filter_by_region_not:
                print("Filtered by Regions (Not) = " + self.flags.filter_by_region_not)

            if self.flags.filter_by_compartment:
                print("Filtered by Compartment like " + self.flags.filter_by_compartment)

            if self.flags.filter_by_compartment_path:
                print("Filtered by Compartment Path = " + self.flags.filter_by_compartment_path)

            if self.flags.filter_by_compartment_recursive:
                print("Filtered by Compartment Recursive = " + self.flags.filter_by_compartment_recursive)

            print("")

            # load identity
            self.__load_section_identity_main()

            # set tenant home region
            self.config['region'] = self.tenancy_home_region
            self.signer.region = self.tenancy_home_region

            # if announcement
            if self.flags.read_announcement:
                self.__load_announcement_main()

            # if cloud guard scores
            if self.flags.read_security:
                self.__load_security_scores_main()

            # check if data not loaded, abort
            if self.C_IDENTITY not in self.data:
                return False

            # check if need to loop on compartments
            # if the flags required data from regions
            if self.flags.is_loop_on_compartments():

                # run on each subscribed region
                tenancy = self.data[self.C_IDENTITY][self.C_IDENTITY_TENANCY]
                for region_name in tenancy['list_region_subscriptions']:

                    # Region Filter
                    if self.flags.filter_by_region:
                        if ',' not in self.flags.filter_by_region:
                            if str(self.flags.filter_by_region) not in region_name:
                                continue
                        else:
                            region_found = False
                            for rg in str(self.flags.filter_by_region).split(","):
                                if rg in region_name:
                                    region_found = True
                            if not region_found:
                                continue

                    # Region Filter Not
                    if self.flags.filter_by_region_not:
                        if ',' not in self.flags.filter_by_region_not:
                            if str(self.flags.filter_by_region_not) in region_name:
                                continue
                        else:
                            region_found = False
                            for rg in str(self.flags.filter_by_region_not).split(","):
                                if rg in region_name:
                                    region_found = True
                            if region_found:
                                continue

                    # load region into data
                    self.__load_oci_region_data(region_name)

            return True

        except Exception as e:
            self.__print_error("__load_data_main: ", e)
            raise

    ##########################################################################
    # run on Region
    ##########################################################################
    def __load_oci_region_data(self, region_name):

        # capture region start time
        region_start_time = time.time()

        # Assign Region to config file
        self.print_header("Region " + region_name, 2)
        self.config['region'] = region_name
        self.signer.region = region_name

        # load ADs
        if self.flags.is_load_basic_network():
            self.__load_section_identity_availability_domain(region_name)

        # Load Network (Threaded) includes load balancers
        if self.flags.is_load_basic_network():
            self.__load_section_core_network_main()

        # if load compute (Threaded)
        if self.flags.read_compute or self.flags.read_containers:
            self.__load_section_core_compute_main()

        # database (Threaded)
        if self.flags.read_database:
            self.__load_section_database_main()

        # Native, data and ai (Threaded)
        if self.flags.read_paas_native or self.flags.read_data_ai:
            self.__load_section_native_data_ai_main()

        # if monitoring, security, limits, quotas, email and budget (Threaded)
        if self.flags.read_monitoring_notifications:
            self.__load_section_monitor_notification_security_quotas_main()

        # if streams, api, fun, orm, queues... (Threaded)
        if self.flags.read_streams_queues or self.flags.read_resource_management or self.flags.read_api or self.flags.read_function:
            self.__load_section_streams_queues_api_fun_orm_main()

        # object storage and File Storage (Thread)
        if self.flags.read_object_storage or self.flags.read_file_storage:
            self.__load_section_object_storage_file_storage_main()

        # if Edge (Thread)
        if self.flags.read_edge:
            self.__load_section_edge_services_main()

        et = time.time() - region_start_time
        print("*** Elapsed Region '" + region_name + "' - " + '{:02d}:{:02d}:{:02d}'.format(round(et // 3600), (round(et % 3600 // 60)), round(et % 60)) + " ***")

    ##########################################################################
    # Identity Module
    ##########################################################################
    def __load_section_identity_main(self):
        try:
            print("Identity... (Main)")
            section_start_time = time.time()

            # create identity object
            identity = oci.identity.IdentityClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            if self.flags.proxy:
                identity.base_client.session.proxies = {'https': self.flags.proxy}

            # get tenancy id from the config file
            tenancy_id = self.get_tenancy_id()
            self.data[self.C_IDENTITY] = {}

            # loading main components - tenancy and compartments
            self.__load_identity_tenancy(identity, tenancy_id)

            # Load single compartment or all
            if 'ocid1.compartment' in self.flags.filter_by_compartment:
                self.__load_identity_single_compartments(identity)
            else:
                self.__load_identity_compartments(identity)

            # if loading the full identity - load the rest
            if self.flags.read_identity:

                # Load Identity Domains
                print("")
                showoci_domains = ShowOCIDomains(self.config, self.signer, self.flags)
                domains_data = showoci_domains.load_identity_domains_main()
                self.error += showoci_domains.error
                self.warning += showoci_domains.warning
                self.data[self.C_IDENTITY][self.C_IDENTITY_DOMAINS] = domains_data

                # if identity domain
                if domains_data:
                    print("Identity (Common)...")
                    self.__load_identity_network_sources(identity, tenancy_id)
                    self.__load_identity_policies(identity)
                    self.__load_identity_cost_tracking_tags(identity, tenancy_id)
                    self.__load_identity_tag_namespace(identity)

                # if no identity domains
                else:
                    print("\nIdentity (No Domains)...")
                    ################
                    # if Serial
                    ################
                    if self.flags.skip_threads:
                        self.__load_identity_users_groups(identity, tenancy_id)
                        self.__load_identity_dynamic_groups(identity, tenancy_id)
                        self.__load_identity_network_sources(identity, tenancy_id)
                        self.__load_identity_policies(identity)
                        self.__load_identity_cost_tracking_tags(identity, tenancy_id)
                        self.__load_identity_tag_namespace(identity)

                    ################
                    # Threads
                    ################
                    else:
                        with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                            future_use = executor.submit(self.__load_identity_users_groups, identity, tenancy_id)
                            future_dyn = executor.submit(self.__load_identity_dynamic_groups, identity, tenancy_id)
                            future_net = executor.submit(self.__load_identity_network_sources, identity, tenancy_id)
                            future_pol = executor.submit(self.__load_identity_policies, identity)
                            future_cos = executor.submit(self.__load_identity_cost_tracking_tags, identity, tenancy_id)
                            future_tag = executor.submit(self.__load_identity_tag_namespace, identity)

                            as_completed([future_use])
                            as_completed([future_dyn])
                            as_completed([future_net])
                            as_completed([future_pol])
                            as_completed([future_cos])
                            as_completed([future_tag])

            print("")
            self.__load_print_section_time(section_start_time)

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_section_identity_main: ", e)

    ##########################################################################
    # Load Tenancy
    # Password policy contributed by Josh.
    ##########################################################################

    def __load_identity_tenancy(self, identity, tenancy_id):
        errstr = ""
        header = "Tenancy"
        self.__load_print_status_with_threads(header)
        start_time = time.time()
        try:
            tenancy = identity.get_tenancy(tenancy_id).data

            # Getting Tenancy Password Policy
            password_policy = {}
            try:
                password_policy_data = identity.get_authentication_policy(tenancy.id).data
                if password_policy_data:
                    ppd = password_policy_data.password_policy
                    password_policy = {
                        'is_lowercase_characters_required': self.get_value(ppd.is_lowercase_characters_required),
                        'is_numeric_characters_required': self.get_value(ppd.is_numeric_characters_required),
                        'is_special_characters_required': self.get_value(ppd.is_special_characters_required),
                        'is_uppercase_characters_required': self.get_value(ppd.is_uppercase_characters_required),
                        'is_username_containment_allowed': self.get_value(ppd.is_username_containment_allowed),
                        'minimum_password_length': self.get_value(ppd.minimum_password_length)
                    }

            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning()
                else:
                    raise

            # Get sub regions
            data_subs = []
            try:
                sub_regions = identity.list_region_subscriptions(tenancy.id).data
                data_subs = [str(es.region_name) for es in sub_regions]
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            # add the data
            data = {
                'id': tenancy.id,
                'name': tenancy.name,
                'home_region_key': tenancy.home_region_key,
                'subscribe_regions': str(', '.join(x for x in data_subs)),
                'list_region_subscriptions': data_subs,
                'password_policy': password_policy
            }

            # home region
            for reg in sub_regions:
                if reg.is_home_region:
                    self.tenancy_home_region = str(reg.region_name)

            self.data[self.C_IDENTITY][self.C_IDENTITY_TENANCY] = data
            cnt = 1
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError as e:
            print("\n*********************************************************************")
            print("* Error Authenticating in __load_identity_tenancy:")
            print("* " + str(e.message))
            print("* Aborting.                                                         *")
            print("*********************************************************************")
            print("")
            raise SystemExit
        except Exception as e:
            raise Exception("Error in __load_identity_tenancy: " + str(e.args))

    ##########################################################################
    # Load compartments
    ##########################################################################
    def __load_identity_compartments(self, identity):

        compartments = []
        errstr = ""
        header = "Compartments"
        self.__load_print_status_with_threads(header)
        start_time = time.time()

        try:
            # point to tenancy
            tenancy = self.data[self.C_IDENTITY][self.C_IDENTITY_TENANCY]

            # read all compartments to variable
            all_compartments = []
            try:
                all_compartments = oci.pagination.list_call_get_all_results(
                    identity.list_compartments,
                    tenancy['id'],
                    compartment_id_in_subtree=True,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            ###################################################
            # Build Compartments
            # return nested compartment list
            ###################################################
            def build_compartments_nested(identity_client, cid, path):
                try:
                    compartment_list = [item for item in all_compartments if str(item.compartment_id) == str(cid)]

                    if path != "":
                        path = path + " / "

                    for c in compartment_list:
                        if c.lifecycle_state == oci.identity.models.Compartment.LIFECYCLE_STATE_ACTIVE:
                            cvalue = {
                                'id': str(c.id),
                                'name': str(c.name),
                                'description': self.get_value(c.description),
                                'time_created': self.get_value(c.time_created),
                                'is_accessible': self.get_value(c.is_accessible),
                                'lifecycle_state': self.get_value(c.lifecycle_state),
                                'inactive_status': self.get_value(c.inactive_status),
                                'path': path + str(c.name),
                                'defined_tags': [] if c.defined_tags is None else c.defined_tags,
                                'freeform_tags': [] if c.freeform_tags is None else c.freeform_tags
                            }
                            compartments.append(cvalue)
                            build_compartments_nested(identity_client, c.id, cvalue['path'])

                except Exception as error:
                    raise Exception("Error in build_compartments_nested: " + str(error.args))

            ###################################################
            # Add root compartment
            ###################################################
            if self.flags.read_root_compartment:
                try:
                    tenc = identity.get_compartment(tenancy['id']).data
                    if tenc:
                        cvalue = {
                            'id': str(tenc.id),
                            'name': str(tenc.name),
                            'description': self.get_value(tenc.description),
                            'time_created': self.get_value(tenc.time_created),
                            'is_accessible': self.get_value(tenc.is_accessible),
                            'lifecycle_state': 'ACTIVE',
                            'inactive_status': "",
                            'path': "/ " + str(tenc.name) + " (root)",
                            'defined_tags': [] if tenc.defined_tags is None else tenc.defined_tags,
                            'freeform_tags': [] if tenc.freeform_tags is None else tenc.freeform_tags
                        }
                        compartments.append(cvalue)
                except Exception as error:
                    raise Exception("Error in add_tenant_compartment: " + str(error.args))

            # Build the compartments
            build_compartments_nested(identity, tenancy['id'], "")

            # sort the compartment
            sorted_compartments = sorted(compartments, key=lambda k: k['path'])

            # if not filtered by compartment return
            if not (self.flags.filter_by_compartment or self.flags.filter_by_compartment_path or self.flags.filter_by_compartment_recursive):
                self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS] = sorted_compartments
                cnt = len(compartments)
                self.__load_print_thread_cnt(header, cnt, start_time, errstr)
                return

            filtered_compart = []

            # if filter by compartment, then reduce list and return new list
            if self.flags.filter_by_compartment:
                for x in sorted_compartments:
                    if self.flags.filter_by_compartment in x['name'] or self.flags.filter_by_compartment in x['id']:
                        filtered_compart.append(x)

            # if filter by path compartment, then reduce list and return new list
            if self.flags.filter_by_compartment_path:
                for x in sorted_compartments:
                    if self.flags.filter_by_compartment_path == x['path']:
                        filtered_compart.append(x)            # if filter by path compartment, then reduce list and return new list

            if self.flags.filter_by_compartment_recursive:
                for x in sorted_compartments:
                    if self.flags.filter_by_compartment_recursive in x['path']:
                        filtered_compart.append(x)

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS] = filtered_compart
            cnt = len(filtered_compart)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            raise Exception("Error in __load_identity_compartments: " + str(e.args))

    ##########################################################################
    # Load single compartment to support BOAT authentication
    ##########################################################################
    def __load_identity_single_compartments(self, identity):

        errstr = ""
        header = "Compartments"
        self.__load_print_status_with_threads(header)
        start_time = time.time()

        compartments = []
        try:

            # read compartments to variable
            compartment = ""
            try:
                compartment = identity.get_compartment(self.flags.filter_by_compartment).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            if compartment:
                cvalue = {
                    'id': str(compartment.id),
                    'name': str(compartment.name),
                    'description': self.get_value(compartment.description),
                    'time_created': self.get_value(compartment.time_created),
                    'is_accessible': self.get_value(compartment.is_accessible),
                    'lifecycle_state': self.get_value(compartment.lifecycle_state),
                    'inactive_status': self.get_value(compartment.inactive_status),
                    'path': str(compartment.name),
                    'defined_tags': [] if compartment.defined_tags is None else compartment.defined_tags,
                    'freeform_tags': [] if compartment.freeform_tags is None else compartment.freeform_tags
                }
                compartments.append(cvalue)

            self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS] = compartments
            cnt = len(compartments)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            raise Exception("Error in __load_identity_single_compartments: " + str(e.args))

    ##########################################################################
    # Get Identity Users
    ##########################################################################

    def __load_identity_users_groups(self, identity, tenancy_id):
        datauser = []
        datagroup = []
        cnt = 0

        errstr = ""
        header = "Groups"
        self.__load_print_status_with_threads(header)
        start_time = time.time()

        try:
            users = []
            groups = []

            try:
                users = oci.pagination.list_call_get_all_results(identity.list_users, tenancy_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                groups = oci.pagination.list_call_get_all_results(identity.list_groups, tenancy_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
            except oci.exceptions.ServiceError as item:
                if 'auth' in item.code.lower() or item.code == 'Forbidden':
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            members = []

            ##########################
            # add groups
            ##########################
            for group in groups:

                if self.flags.skip_threads:
                    if cnt % 10 == 0:
                        print("g", end="")
                cnt += 1

                try:
                    user_group_memberships = oci.pagination.list_call_get_all_results(
                        identity.list_user_group_memberships, tenancy_id, group_id=group.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                    group_users = []
                    for ugm in user_group_memberships:
                        members.append({'user_id': ugm.user_id, 'group_id': ugm.group_id})
                        for item in [str(item_var.name) for item_var in users if item_var.id == ugm.user_id]:
                            group_users.append(item)

                    datagroup.append({'id': group.id, 'name': group.name, 'users': ', '.join(x for x in group_users)})

                except oci.exceptions.ServiceError as error:
                    if 'auth' in error.code.lower() or error.code == 'Forbidden':
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

            # load to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_GROUPS] = datagroup
            cnt = len(datagroup)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            ##########################
            # add users
            ##########################
            errstr = ""
            header = "Users"
            self.__load_print_status_with_threads(header)
            start_time = time.time()
            cnt = 0

            for user in users:

                group_users = []
                if self.flags.skip_threads:
                    if cnt % 10 == 0:
                        print("u", end="")
                cnt += 1

                # find the group users
                for ugm in [e['group_id'] for e in members if user.id == e['user_id']]:
                    group_users.append(next(item for item in groups if item.id == ugm).name)

                # user data
                user_data = {
                    'id': user.id,
                    'name': str(user.name),
                    'description': self.get_value(user.description),
                    'is_mfa_activated': self.get_value(user.is_mfa_activated),
                    'lifecycle_state': self.get_value(user.lifecycle_state),
                    'inactive_status': self.get_value(user.inactive_status),
                    'time_created': self.get_value(user.time_created),
                    'identity_provider_id': "",
                    'identity_provider_name': "",
                    'email': self.get_value(user.email),
                    'email_verified': self.get_value(user.email_verified),
                    'external_identifier': self.get_value(user.external_identifier),
                    'last_successful_login_time': self.get_value(user.last_successful_login_time),
                    'previous_successful_login_time': self.get_value(user.previous_successful_login_time),
                    'groups': ', '.join(x for x in group_users),
                    'capabilities': user.capabilities
                }

                if user.capabilities:
                    user_data['capabilities'] = {
                        'can_use_console_password': self.get_value(user.capabilities.can_use_console_password),
                        'can_use_api_keys': self.get_value(user.capabilities.can_use_api_keys),
                        'can_use_auth_tokens': self.get_value(user.capabilities.can_use_auth_tokens),
                        'can_use_smtp_credentials': self.get_value(user.capabilities.can_use_smtp_credentials),
                        'can_use_customer_secret_keys': self.get_value(user.capabilities.can_use_customer_secret_keys),
                        'can_use_o_auth2_client_credentials': self.get_value(user.capabilities.can_use_o_auth2_client_credentials)
                    }

                # get the credential for the user
                if not self.flags.skip_identity_user_credential:
                    if self.flags.skip_threads:
                        user_data['api_keys'] = self.__load_identity_user_credentials_apikey(identity, user)
                        user_data['auth_token'] = self.__load_identity_user_credentials_token(identity, user)
                        user_data['secret_key'] = self.__load_identity_user_credentials_secret(identity, user)
                        user_data['smtp_cred'] = self.__load_identity_user_credentials_smtp(identity, user)
                    else:
                        # if parallel execution
                        with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                            future_api_keys = executor.submit(self.__load_identity_user_credentials_apikey, identity, user)
                            future_auth_token = executor.submit(self.__load_identity_user_credentials_token, identity, user)
                            future_secret_key = executor.submit(self.__load_identity_user_credentials_secret, identity, user)
                            future_smtp_cred = executor.submit(self.__load_identity_user_credentials_smtp, identity, user)

                            user_data['api_keys'] = next(as_completed([future_api_keys])).result()
                            user_data['auth_token'] = next(as_completed([future_auth_token])).result()
                            user_data['secret_key'] = next(as_completed([future_secret_key])).result()
                            user_data['smtp_cred'] = next(as_completed([future_smtp_cred])).result()

                datauser.append(user_data)

            # load to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_USERS] = datauser
            cnt = len(datauser)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException:
            raise
        except Exception as e:
            self.__print_error("__load_identity_users_groups", e)

    ########################################################
    # Contributed by J.Hammer
    # Add User API Keys
    ########################################################
    def __load_identity_user_credentials_apikey(self, identity, user):

        datauserapikey = []

        try:
            user_api_keys = oci.pagination.list_call_get_all_results(
                identity.list_api_keys,
                user.id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # add user api keys
            if user_api_keys:
                for api_key in user_api_keys:
                    datauserapikey.append({
                        'id': api_key.key_id,
                        'inactive_status': self.get_value(api_key.inactive_status),
                        'lifecycle_state': self.get_value(api_key.lifecycle_state),
                        'time_created': self.get_value(api_key.time_created)
                    })

            # return the data
            return datauserapikey

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                if self.flags.skip_threads:
                    self.__load_print_auth_warning('c')
                pass
            else:
                raise

        except Exception as e:
            self.__print_error("__load_identity_user_credentials_apikey", e)

    ########################################################
    # Contributed by J.Hammer
    # Add User Tokens
    ########################################################
    def __load_identity_user_credentials_token(self, identity, user):

        datauserauthtoken = []

        ##################
        # Auth Token
        ##################
        try:
            user_auth_tokens = oci.pagination.list_call_get_all_results(
                identity.list_auth_tokens,
                user.id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # add user auth tokens
            if user_auth_tokens:
                for token in user_auth_tokens:
                    datauserauthtoken.append({
                        'id': token.id,
                        'description': token.description,
                        'lifecycle_state': self.get_value(token.lifecycle_state),
                        'inactive_status': self.get_value(token.inactive_status),
                        'time_created': self.get_value(token.time_created),
                        'time_expires': self.get_value(token.time_expires),
                        'token': token.token
                    })

            return datauserauthtoken

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                if self.flags.skip_threads:
                    self.__load_print_auth_warning('c')
                pass
            else:
                raise

        except Exception as e:
            self.__print_error("__load_identity_user_credentials_token", e)

    ########################################################
    # Contributed by J.Hammer
    # Add User Secrets
    ########################################################
    def __load_identity_user_credentials_secret(self, identity, user):

        datausersecretkey = []

        try:
            user_secret_keys = oci.pagination.list_call_get_all_results(
                identity.list_customer_secret_keys,
                user.id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # add user secret keys
            if user_secret_keys:
                for secret in user_secret_keys:
                    datausersecretkey.append({
                        'id': secret.id,
                        'display_name': secret.display_name,
                        'lifecycle_state': self.get_value(secret.lifecycle_state),
                        'inactive_status': self.get_value(secret.inactive_status),
                        'time_created': self.get_value(secret.time_created),
                        'time_expires': self.get_value(secret.time_expires)
                    })
            return datausersecretkey

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                if self.flags.skip_threads:
                    self.__load_print_auth_warning('c')
                pass
            else:
                raise

        except Exception as e:
            self.__print_error("__load_identity_user_credentials_secret", e)

    ########################################################
    # Contributed by J.Hammer
    # Add User SMTP Creds
    ########################################################
    def __load_identity_user_credentials_smtp(self, identity, user):

        datausersmtpcred = []

        try:
            user_smtp_creds = oci.pagination.list_call_get_all_results(
                identity.list_smtp_credentials,
                user.id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # add user secret keys
            if user_smtp_creds:
                for smtp_creds in user_smtp_creds:
                    datausersmtpcred.append({
                        'id': smtp_creds.id,
                        'description': smtp_creds.description,
                        'lifecycle_state': self.get_value(smtp_creds.lifecycle_state),
                        'inactive_status': self.get_value(smtp_creds.inactive_status),
                        'time_created': self.get_value(smtp_creds.time_created),
                        'time_expires': self.get_value(smtp_creds.time_expires),
                        'username': smtp_creds.username
                    })

            return datausersmtpcred

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                if self.flags.skip_threads:
                    self.__load_print_auth_warning('c')
                pass
            else:
                raise

        except Exception as e:
            self.__print_error("__load_identity_user_credentials_smtp", e)

    ##########################################################################
    # Print Identity Policies
    ##########################################################################
    def __load_identity_policies(self, identity):
        data = []
        errstr = ""
        header = "Policies"
        self.__load_print_status_with_threads(header)
        start_time = time.time()

        try:
            compartments = self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS]

            for c in compartments:
                if self.__if_managed_paas_compartment(c['name']) and not self.flags.read_ManagedCompartmentForPaaS:
                    continue

                try:
                    policies = oci.pagination.list_call_get_all_results(identity.list_policies, c['id'], retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                    if policies:
                        datapol = []
                        for policy in policies:
                            datapol.append({
                                'name': policy.name,
                                'id': policy.id,
                                'statements': [str(e) for e in policy.statements]
                            })

                        dataval = {
                            'compartment_id': str(c['id']),
                            'compartment_name': c['name'],
                            'compartment_path': c['path'],
                            'policies': datapol
                        }
                        data.append(dataval)

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_POLICIES] = data
            cnt = len(data)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_policies", e)

    ##########################################################################
    # Print Dynamic Groups
    ##########################################################################
    def __load_identity_dynamic_groups(self, identity, tenancy_id):

        data = []
        errstr = ""
        header = "Dynamic Groups"
        self.__load_print_status_with_threads(header)
        start_time = time.time()

        try:
            dynamic_groups = []
            try:
                dynamic_groups = oci.pagination.list_call_get_all_results(identity.list_dynamic_groups, tenancy_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            for dg in dynamic_groups:
                # print(".", end="")
                data.append({
                    'id': str(dg.id),
                    'name': str(dg.name),
                    'description': str(dg.description),
                    'matching_rule': str(dg.matching_rule)
                })

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_DYNAMIC_GROUPS] = data
            cnt = len(data)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_dynamic_groups", e)

    ##########################################################################
    # Load Network Sources
    ##########################################################################
    def __load_identity_network_sources(self, identity, tenancy_id):

        data = []
        errstr = ""
        header = "Network Sources"
        self.__load_print_status_with_threads(header)
        start_time = time.time()

        try:
            network_sources = []
            try:
                network_sources = oci.pagination.list_call_get_all_results(identity.list_network_sources, tenancy_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            # oci.identity.models.NetworkSourcesSummary
            for ns in network_sources:
                #   print(".", end="")

                # compile vcn ip list
                vcn_list = []
                for vcn in ns.virtual_source_list:
                    vcn_list.append({
                        'vcn_id': vcn.vcn_id,
                        'ip_ranges': str(', '.join(x for x in vcn.ip_ranges)),
                    })

                data.append({
                    'id': str(ns.id),
                    'name': str(ns.name),
                    'description': str(ns.description),
                    'virtual_source_list': vcn_list,
                    'public_source_list': ns.public_source_list,
                    'services': ns.services,
                    'time_created': str(ns.time_created)
                })

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_NETWORK_SOURCES] = data
            cnt = len(data)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_network_sources", e)

    ##########################################################################
    # load cost tracking tags
    ##########################################################################
    def __load_identity_cost_tracking_tags(self, identity, tenancy_id):

        data = []
        errstr = ""
        header = "Cost Tracking Tags"
        self.__load_print_status_with_threads(header)
        start_time = time.time()

        try:
            tags = []
            try:
                tags = oci.pagination.list_call_get_all_results(identity.list_cost_tracking_tags, tenancy_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            # tag = oci.identity.models.Tag
            for tag in tags:
                dataval = {'tag_namespace_id': str(tag.tag_namespace_id),
                           'tag_namespace_name': str(tag.tag_namespace_name),
                           'id': str(tag.id),
                           'name': str(tag.name),
                           'description': self.get_value(tag.description),
                           'is_retired': self.get_value(tag.is_retired),
                           'time_created': self.get_value(tag.time_created),
                           'is_cost_tracking': self.get_value(tag.is_cost_tracking)
                           }
                data.append(dataval)

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_COST_TRACKING_TAGS] = data
            cnt = len(data)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_cost_tracking_tags", e)

    ##########################################################################
    # Load Tag Namespace
    ##########################################################################
    def __load_identity_tag_namespace(self, identity):
        data = []
        errstr = ""
        header = "Tag Namespace"
        self.__load_print_status_with_threads(header)
        start_time = time.time()

        try:
            compartments = self.data[self.C_IDENTITY][self.C_IDENTITY_COMPARTMENTS]

            for c in compartments:
                #   print(".", end="")
                if self.__if_managed_paas_compartment(c['name']) and not self.flags.read_ManagedCompartmentForPaaS:
                    continue

                try:
                    tags = oci.pagination.list_call_get_all_results(
                        identity.list_tag_namespaces, c['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                    if tags:

                        # prepare compartment
                        dataval = {
                            'compartment_id': str(c['id']),
                            'compartment_name': c['name'],
                            'compartment_path': c['path'],
                            'tags': []
                        }

                        # Add tags
                        for tag in tags:
                            val = {
                                'id': tag.id,
                                'name': str(tag.name),
                                'description': self.get_value(tag.description),
                                'is_retired': self.get_value(tag.is_retired),
                                'lifecycle_state': self.get_value(tag.lifecycle_state),
                                'time_created': self.get_value(tag.time_created),
                                'defined_tags': [] if tag.defined_tags is None else tag.defined_tags,
                                'freeform_tags': [] if tag.freeform_tags is None else tag.freeform_tags
                            }
                            dataval['tags'].append(val)

                        if dataval['tags']:
                            data.append(dataval)

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_TAG_NAMESPACE] = data
            cnt = len(data)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_tag_namespace", e)

    ##########################################################################
    # Load Identity Availability Domains
    ##########################################################################
    def __load_section_identity_availability_domain(self, region_name):

        try:
            print("Identity...")

            # create identity object
            identity = oci.identity.IdentityClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            if self.flags.proxy:
                identity.base_client.session.proxies = {'https': self.flags.proxy}

            errstr = ""
            header = "Availability Domains"
            self.__load_print_status_with_threads(header)
            start_time = time.time()

            # initalize the key
            self.__initialize_data_key(self.C_IDENTITY, self.C_IDENTITY_ADS)

            # get the domains
            availability_domains = []
            try:
                availability_domains = identity.list_availability_domains(self.get_tenancy_id()).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            data = []
            cnt = 0
            for ad in availability_domains:
                data.append({'region_name': region_name, 'id': str(ad.id), 'name': str(ad.name)})
                cnt += 1

            # add to data
            self.data[self.C_IDENTITY][self.C_IDENTITY_ADS] += data

            # mark count
            cnt = len(data)
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            print("")

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_section_identity_availability_domain", e)

    ##########################################################################
    # Load all networks to data
    ##########################################################################
    def __load_section_core_network_main(self):

        try:
            # if to exclude network
            if self.EXCLUDE_NETWORK in self.flags.exclude:
                return

            print("Network...")

            section_start_time = time.time()

            # Open connectivity to OCI
            virtual_network = oci.core.VirtualNetworkClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            dns_client = oci.dns.DnsClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            nwf_client = oci.network_firewall.NetworkFirewallClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            load_balancer = oci.load_balancer.LoadBalancerClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            network_load_balancer = oci.network_load_balancer.NetworkLoadBalancerClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}
                dns_client.base_client.session.proxies = {'https': self.flags.proxy}
                nwf_client.base_client.session.proxies = {'https': self.flags.proxy}
                load_balancer.base_client.session.proxies = {'https': self.flags.proxy}
                network_load_balancer.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key to the network if not exists
            self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_VCN)
            self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_SUBNET)
            self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_NSG)

            # if to load all network resources initialize the keys
            if self.flags.read_network:

                # add the key to the network if not exists
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_SUBNET_PIP)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_VLAN)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_SGW)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_NAT)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_DRG)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_DRG_AT)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_DRG_RT)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_CPE)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_IPS)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_RPC)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_VC)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_IGW)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_LPG)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_ROUTE)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_SLIST)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_DHCP)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_PRIVATEIP)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_DNS_RESOLVERS)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_FIREWALL)
                self.__initialize_data_key(self.C_NETWORK, self.C_NETWORK_FIREWALL_POLICY)
                self.__initialize_data_key(self.C_LB, self.C_LB_LOAD_BALANCERS)
                self.__initialize_data_key(self.C_LB, self.C_LB_BACKEND_SETS)
                self.__initialize_data_key(self.C_LB, self.C_LB_NETWORK_LOAD_BALANCERS)
                self.__initialize_data_key(self.C_LB, self.C_LB_NETWORK_BACKEND_SETS)

            # reference to network and initial variables:
            network = self.data[self.C_NETWORK]

            ##########################
            # if serial execution
            ##########################
            if self.flags.skip_threads:
                vcns = self.__load_core_network_vcn(virtual_network, compartments)
                subnets = self.__load_core_network_subnet(virtual_network, compartments)
                nsg = self.__load_core_network_nsg(virtual_network, compartments)

                network[self.C_NETWORK_VCN] += vcns
                network[self.C_NETWORK_SUBNET] += subnets
                network[self.C_NETWORK_NSG] += nsg

                # merge vcn info to subnets
                self.__load_core_network_subnet_add_vcn_info()

                # mark if vcn exist for this regiot
                self.is_vcn_exist_for_region = (len(vcns) > 0)

                # read network resources only if there are vcns
                if self.is_vcn_exist_for_region and self.flags.read_network:

                    network[self.C_NETWORK_SUBNET_PIP] += self.__load_core_network_subnet_private_ip(virtual_network, subnets)
                    network[self.C_NETWORK_VLAN] += self.__load_core_network_vlan(virtual_network, compartments)
                    network[self.C_NETWORK_LPG] += self.__load_core_network_lpg(virtual_network, compartments)
                    network[self.C_NETWORK_SGW] += self.__load_core_network_sgw(virtual_network, compartments)
                    network[self.C_NETWORK_NAT] += self.__load_core_network_nat(virtual_network, compartments)
                    network[self.C_NETWORK_DRG_AT] += self.__load_core_network_dra(virtual_network, compartments)
                    network[self.C_NETWORK_DRG] += self.__load_core_network_drg(virtual_network, compartments)
                    network[self.C_NETWORK_CPE] += self.__load_core_network_cpe(virtual_network, compartments)
                    network[self.C_NETWORK_IPS] += self.__load_core_network_ips(virtual_network, compartments)
                    network[self.C_NETWORK_RPC] += self.__load_core_network_rpc(virtual_network, compartments)
                    network[self.C_NETWORK_VC] += self.__load_core_network_vc(virtual_network, compartments)
                    network[self.C_NETWORK_IGW] += self.__load_core_network_igw(virtual_network, compartments)
                    network[self.C_NETWORK_SLIST] += self.__load_core_network_seclst(virtual_network, compartments)
                    network[self.C_NETWORK_DHCP] += self.__load_core_network_dhcpop(virtual_network, compartments)
                    network[self.C_NETWORK_DNS_RESOLVERS] += self.__load_core_network_dns_resolvers(dns_client, compartments)
                    network[self.C_NETWORK_FIREWALL_POLICY] += self.__load_core_network_firewall_policy(nwf_client, compartments)
                    network[self.C_NETWORK_FIREWALL] += self.__load_core_network_firewall(nwf_client, compartments)

                    routes = self.__load_core_network_routet(virtual_network, compartments)
                    network[self.C_NETWORK_ROUTE] += routes
                    network[self.C_NETWORK_PRIVATEIP] += self.__load_core_network_privateip(virtual_network, routes)

                    lb = self.data[self.C_LB]
                    lb[self.C_LB_LOAD_BALANCERS] += self.__load_load_balancers(load_balancer, compartments)
                    lb[self.C_LB_BACKEND_SETS] += self.__load_load_balancer_backendset(load_balancer)
                    lb[self.C_LB_NETWORK_LOAD_BALANCERS] += self.__load_load_balancers_network(network_load_balancer, compartments)
                    lb[self.C_LB_NETWORK_BACKEND_SETS] += self.__load_load_balancer_backendset_network(network_load_balancer)

            ##########################
            # if parallel execution
            ##########################
            else:
                with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                    future_vcn = executor.submit(self.__load_core_network_vcn, virtual_network, compartments)
                    future_subnet = executor.submit(self.__load_core_network_subnet, virtual_network, compartments)
                    future_nsg = executor.submit(self.__load_core_network_nsg, virtual_network, compartments)

                    # Wait for completion
                    vcns = next(as_completed([future_vcn])).result()
                    subnets = next(as_completed([future_subnet])).result()
                    nsg = next(as_completed([future_nsg])).result()

                    network[self.C_NETWORK_VCN] += vcns
                    network[self.C_NETWORK_SUBNET] += subnets
                    network[self.C_NETWORK_NSG] += nsg

                    # merge vcn info to subnets
                    self.__load_core_network_subnet_add_vcn_info()

                    # mark if vcn exist for this region
                    self.is_vcn_exist_for_region = (len(vcns) > 0)

                    future_network_routes = None
                    future_network_vir = None
                    future_network_dns = None
                    future_network_igw = None
                    future_network_pip = None
                    future_network_vlan = None
                    future_network_lpg = None
                    future_network_sgw = None
                    future_network_nat = None
                    future_network_dra = None
                    future_network_drg = None
                    future_network_cpe = None
                    future_network_ips = None
                    future_network_rpc = None
                    future_network_slt = None
                    future_network_dhcp = None
                    future_network_fwp = None
                    future_network_fw = None
                    future_LB_LOAD_BALANCERS = None
                    future_LB_NETWORK_LOAD_BALANCERS = None
                    future_LB_BACKEND_SETS = None
                    future_LB_NETWORK_BACKEND_SETS = None

                    # read network resources only if there are vcns
                    if self.is_vcn_exist_for_region and self.flags.read_network:

                        # Run in parallel
                        future_network_routes = executor.submit(self.__load_core_network_routet, virtual_network, compartments)
                        future_network_vir = executor.submit(self.__load_core_network_vc, virtual_network, compartments)
                        future_network_dns = executor.submit(self.__load_core_network_dns_resolvers, dns_client, compartments)
                        future_network_igw = executor.submit(self.__load_core_network_igw, virtual_network, compartments)
                        future_network_subip = executor.submit(self.__load_core_network_subnet_private_ip, virtual_network, subnets)
                        future_network_vlan = executor.submit(self.__load_core_network_vlan, virtual_network, compartments)
                        future_network_lpg = executor.submit(self.__load_core_network_lpg, virtual_network, compartments)
                        future_network_sgw = executor.submit(self.__load_core_network_sgw, virtual_network, compartments)
                        future_network_nat = executor.submit(self.__load_core_network_nat, virtual_network, compartments)
                        future_network_dra = executor.submit(self.__load_core_network_dra, virtual_network, compartments)
                        future_network_drg = executor.submit(self.__load_core_network_drg, virtual_network, compartments)
                        future_network_cpe = executor.submit(self.__load_core_network_cpe, virtual_network, compartments)
                        future_network_ips = executor.submit(self.__load_core_network_ips, virtual_network, compartments)
                        future_network_rpc = executor.submit(self.__load_core_network_rpc, virtual_network, compartments)
                        future_network_slt = executor.submit(self.__load_core_network_seclst, virtual_network, compartments)
                        future_network_dhcp = executor.submit(self.__load_core_network_dhcpop, virtual_network, compartments)
                        future_network_fwp = executor.submit(self.__load_core_network_firewall_policy, nwf_client, compartments)
                        future_network_fw = executor.submit(self.__load_core_network_firewall, nwf_client, compartments)

                        future_LB_LOAD_BALANCERS = executor.submit(self.__load_load_balancers, load_balancer, compartments)
                        future_LB_NETWORK_LOAD_BALANCERS = executor.submit(self.__load_load_balancers_network, network_load_balancer, compartments)

                        # Wait for completion
                        routes = next(as_completed([future_network_routes])).result()
                        network[self.C_NETWORK_ROUTE] += routes

                        # depends on routes execute now
                        future_network_pip = executor.submit(self.__load_core_network_privateip, virtual_network, routes)

                        lb = self.data[self.C_LB]
                        lb[self.C_LB_LOAD_BALANCERS] += next(as_completed([future_LB_LOAD_BALANCERS])).result()
                        lb[self.C_LB_NETWORK_LOAD_BALANCERS] += next(as_completed([future_LB_NETWORK_LOAD_BALANCERS])).result()

                        # Pending main load balancers
                        future_LB_BACKEND_SETS = executor.submit(self.__load_load_balancer_backendset, load_balancer)
                        future_LB_NETWORK_BACKEND_SETS = executor.submit(self.__load_load_balancer_backendset_network, network_load_balancer)

                        # Wait for completion
                        network[self.C_NETWORK_SUBNET_PIP] += next(as_completed([future_network_subip])).result()
                        network[self.C_NETWORK_VLAN] += next(as_completed([future_network_vlan])).result()
                        network[self.C_NETWORK_LPG] += next(as_completed([future_network_lpg])).result()
                        network[self.C_NETWORK_SGW] += next(as_completed([future_network_sgw])).result()
                        network[self.C_NETWORK_NAT] += next(as_completed([future_network_nat])).result()
                        network[self.C_NETWORK_DRG_AT] += next(as_completed([future_network_dra])).result()
                        network[self.C_NETWORK_DRG] += next(as_completed([future_network_drg])).result()
                        network[self.C_NETWORK_CPE] += next(as_completed([future_network_cpe])).result()
                        network[self.C_NETWORK_IPS] += next(as_completed([future_network_ips])).result()
                        network[self.C_NETWORK_RPC] += next(as_completed([future_network_rpc])).result()
                        network[self.C_NETWORK_VC] += next(as_completed([future_network_vir])).result()
                        network[self.C_NETWORK_IGW] += next(as_completed([future_network_igw])).result()
                        network[self.C_NETWORK_SLIST] += next(as_completed([future_network_slt])).result()
                        network[self.C_NETWORK_DHCP] += next(as_completed([future_network_dhcp])).result()
                        network[self.C_NETWORK_DNS_RESOLVERS] += next(as_completed([future_network_dns])).result()
                        network[self.C_NETWORK_FIREWALL_POLICY] += next(as_completed([future_network_fwp])).result()
                        network[self.C_NETWORK_FIREWALL] += next(as_completed([future_network_fw])).result()
                        network[self.C_NETWORK_PRIVATEIP] += next(as_completed([future_network_pip])).result()

                        lb[self.C_LB_BACKEND_SETS] += next(as_completed([future_LB_BACKEND_SETS])).result()
                        lb[self.C_LB_NETWORK_BACKEND_SETS] += next(as_completed([future_LB_NETWORK_BACKEND_SETS])).result()

            self.__load_print_section_time(section_start_time)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_section_core_network_main", e)
            raise

    ##########################################################################
    # data network read vcns - 3/6/2023
    ##########################################################################
    def __load_core_network_vcn(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()
        try:
            errstr = ""
            header = "Virtual Cloud Networks"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                vcns = []
                try:
                    vcns = oci.pagination.list_call_get_all_results(
                        virtual_network.list_vcns,
                        compartment['id'],
                        lifecycle_state=oci.core.models.Vcn.LIFECYCLE_STATE_AVAILABLE,
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on the array
                # vcn = oci.core.models.Vcn()
                for vcn in vcns:
                    val = {
                        'id': str(vcn.id),
                        'name': str(', '.join(x for x in vcn.cidr_blocks)) + " - " + str(vcn.display_name) + " - " + str(vcn.vcn_domain_name),
                        'display_name': str(vcn.display_name),
                        'cidr_block': '',
                        'cidr_blocks': vcn.cidr_blocks,
                        'ipv6_private_cidr_blocks': vcn.ipv6_private_cidr_blocks,
                        'ipv6_cidr_blocks': vcn.ipv6_cidr_blocks,
                        'byoipv6_cidr_blocks': vcn.byoipv6_cidr_blocks,
                        'default_dhcp_options_id': self.get_value(vcn.default_dhcp_options_id),
                        'default_route_table_id': self.get_value(vcn.default_route_table_id),
                        'default_security_list_id': self.get_value(vcn.default_security_list_id),
                        'dns_label': self.get_value(vcn.dns_label),
                        'time_created': self.get_value(vcn.time_created),
                        'vcn_domain_name': self.get_value(vcn.vcn_domain_name),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'defined_tags': [] if vcn.defined_tags is None else vcn.defined_tags,
                        'freeform_tags': [] if vcn.freeform_tags is None else vcn.freeform_tags,
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_vcn", e, compartment)
            return data

    ##########################################################################
    # __load_core_network_vlan
    ##########################################################################
    def __load_core_network_vlan(self, virtual_network, compartments):

        cnt = 0
        data = []
        start_time = time.time()

        try:

            errstr = ""
            header = "VLANs"
            self.__load_print_status_with_threads(header)

            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                vlans = []
                try:
                    vlans = oci.pagination.list_call_get_all_results(
                        virtual_network.list_vlans,
                        compartment['id'],
                        lifecycle_state=oci.core.models.Vlan.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if 'not whitelisted' in str(e.message).lower():
                        print(" tenant not enabled for this region, skipped.")
                        return data
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning('a', False, to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                for vlan in vlans:
                    val = {'id': str(vlan.id),
                           'vlan': str(vlan.vlan_tag) + " - " + str(vlan.cidr_block) + " - " + str(vlan.display_name),
                           'availability_domain': self.get_value(vlan.availability_domain),
                           'cidr_block': self.get_value(vlan.cidr_block),
                           'vlan_tag': self.get_value(vlan.vlan_tag),
                           'display_name': self.get_value(vlan.display_name),
                           'time_created': self.get_value(vlan.time_created),
                           'lifecycle_state': self.get_value(vlan.lifecycle_state),
                           'nsg_ids': vlan.nsg_ids,
                           'route_table_id': self.get_value(vlan.route_table_id),
                           'vcn_id': self.get_value(vlan.vcn_id),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if vlan.defined_tags is None else vlan.defined_tags,
                           'freeform_tags': [] if vlan.freeform_tags is None else vlan.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            if 'NotAuthorizedOrNotFound' in str(e.message):
                return data
            self.__print_error("__load_core_network_vlan", e, compartment)
            return data

    ##########################################################################
    # data network read igw - 3/6/2023
    ##########################################################################
    def __load_core_network_igw(self, virtual_network, compartments):

        cnt = 0
        data = []
        start_time = time.time()

        try:

            errstr = ""
            header = "Internet Gateways"
            self.__load_print_status_with_threads(header)

            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                igws = []
                try:
                    igws = oci.pagination.list_call_get_all_results(
                        virtual_network.list_internet_gateways,
                        compartment['id'],
                        lifecycle_state=oci.core.models.InternetGateway.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                    raise

                for igw in igws:
                    val = {'id': str(igw.id),
                           'vcn_id': str(igw.vcn_id),
                           'name': str(igw.display_name),
                           'is_enabled': self.get_value(igw.is_enabled),
                           'route_table_id': self.get_value(igw.route_table_id),
                           'time_created': self.get_value(igw.time_created),
                           'defined_tags': [] if igw.defined_tags is None else igw.defined_tags,
                           'freeform_tags': [] if igw.freeform_tags is None else igw.freeform_tags,
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])
                           }

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_core_network_igw", e, compartment)
            return data

    ##########################################################################
    # data network lpg - 3/6/2023
    ##########################################################################
    def __load_core_network_lpg(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Local Peer GWs"
            self.__load_print_status_with_threads(header)

            # Loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                local_peering_gateways = []
                try:
                    local_peering_gateways = virtual_network.list_local_peering_gateways(
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                    raise

                # lpg = oci.core.models.LocalPeeringGateway()
                for lpg in local_peering_gateways:
                    if lpg.lifecycle_state != oci.core.models.LocalPeeringGateway.LIFECYCLE_STATE_AVAILABLE:
                        continue

                    # get the cidr block of the peering
                    cidr = "" if lpg.peer_advertised_cidr is None else " - " + str(lpg.peer_advertised_cidr)
                    cidr += "" if not lpg.peer_advertised_cidr_details else " (" + str(', '.join(x for x in lpg.peer_advertised_cidr_details)) + ")"

                    # add lpg info to data
                    val = {'id': str(lpg.id),
                           'vcn_id': str(lpg.vcn_id),
                           'name': str(lpg.peering_status).ljust(8) + " - " + str(lpg.display_name) + str(cidr),
                           'peering_status': self.get_value(lpg.peering_status),
                           'time_created': self.get_value(lpg.time_created),
                           'display_name': self.get_value(lpg.display_name),
                           'peer_advertised_cidr': self.get_value(lpg.peer_advertised_cidr),
                           'is_cross_tenancy_peering': self.get_value(lpg.is_cross_tenancy_peering),
                           'peer_advertised_cidr_details': lpg.peer_advertised_cidr_details,
                           'route_table_id': self.get_value(lpg.route_table_id),
                           'peer_id': self.get_value(lpg.peer_id),
                           'peering_status_details': self.get_value(lpg.peering_status_details),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if lpg.defined_tags is None else lpg.defined_tags,
                           'freeform_tags': [] if lpg.freeform_tags is None else lpg.freeform_tags,
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_lpg", e, compartment)
            return data

    ##########################################################################
    # data network lpg
    ##########################################################################
    def __load_core_network_rpc(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Remote Peer Conns"
            self.__load_print_status_with_threads(header)

            # iLoop on all compartments
            for compartment in compartments:

                rpcs = []
                try:
                    rpcs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_remote_peering_connections,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # rpc = oci.core.models.RemotePeeringConnection()
                for rpc in rpcs:
                    if rpc.lifecycle_state != oci.core.models.RemotePeeringConnection.LIFECYCLE_STATE_AVAILABLE:
                        continue

                    val = {'id': str(rpc.id), 'peer_id': str(rpc.peer_id),
                           'drg_id': self.get_value(rpc.drg_id),
                           'name': self.get_value(rpc.display_name),
                           'time_created': self.get_value(rpc.time_created),
                           'is_cross_tenancy_peering': str(rpc.is_cross_tenancy_peering),
                           'peer_region_name': self.get_value(rpc.peer_region_name),
                           'peer_tenancy_id': self.get_value(rpc.peer_tenancy_id),
                           'peering_status': self.get_value(rpc.peering_status),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region']),
                           'drg_route_table_id': "",
                           'drg_route_table': ""
                           }

                    # find Attachment for the RPC
                    drg_attachment = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_DRG_AT, 'rpc_id', rpc.id)
                    if drg_attachment:
                        val['drg_route_table_id'] = drg_attachment['drg_route_table_id']
                        val['drg_route_table'] = self.get_network_drg_route_table(drg_attachment['drg_route_table_id'])

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_rpc", e, compartment)
            return data

    ##########################################################################
    # data network read route
    ##########################################################################
    def __load_core_network_routet(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Route Tables"
            self.__load_print_status_with_threads(header)

            # Loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                route_tables = []
                try:
                    route_tables = oci.pagination.list_call_get_all_results(
                        virtual_network.list_route_tables,
                        compartment['id'],
                        lifecycle_state=oci.core.models.RouteTable.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # loop on the routes
                # rt = oci.core.models.RouteTable()
                for rt in route_tables:
                    val = {'id': str(rt.id), 'vcn_id': str(rt.vcn_id), 'name': str(rt.display_name),
                           'time_created': str(rt.time_created),
                           'route_rules': [
                               {
                                   'destination': self.get_value(es.destination),
                                   'network_entity_id': self.get_value(es.network_entity_id),
                                   'cidr_block': self.get_value(es.cidr_block),
                                   'description': self.get_value(es.description),
                                   'destination_type': self.get_value(es.destination_type)
                               } for es in rt.route_rules],
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'defined_tags': [] if rt.defined_tags is None else rt.defined_tags,
                           'freeform_tags': [] if rt.freeform_tags is None else rt.freeform_tags,
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_route", e, compartment)
            return data

    ##########################################################################
    # get DHCP options for DHCP_ID
    ##########################################################################
    def __load_core_network_dhcpop_opt(self, dhcp_option):

        retstr = ""
        try:
            opt = dhcp_option

            # if type = oci.core.models.DhcpDnsOption
            if isinstance(opt, oci.core.models.DhcpDnsOption):
                retstr += str(opt.type).ljust(17) + ": " + str(opt.server_type)
                if len(opt.custom_dns_servers) > 0:
                    retstr += " - "
                    for ip in opt.custom_dns_servers:
                        retstr += str(ip) + "  "

            # if type = oci.core.models.DhcpSearchDomainOption
            if isinstance(opt, oci.core.models.DhcpSearchDomainOption):
                if len(opt.search_domain_names) > 0:
                    retstr += str(opt.type).ljust(17) + ": "
                    for ip in opt.search_domain_names:
                        retstr += str(ip) + "  "

            return retstr

        except Exception as e:
            self.__print_error("__load_core_network_dhcpop_opt", e)
            return retstr

    ##########################################################################
    # data network read dhcp options
    ##########################################################################
    def __load_core_network_dhcpop(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "DHCP Options"
            self.__load_print_status_with_threads(header)

            # Loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                dhcp_options = []
                try:
                    dhcp_options = oci.pagination.list_call_get_all_results(
                        virtual_network.list_dhcp_options,
                        compartment['id'],
                        lifecycle_state=oci.core.models.DhcpOptions.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # loop on the routes
                # dhcp = oci.core.models.DhcpOptions()
                for dhcp in dhcp_options:

                    # Analyzing DHCP Option
                    dhcp_opt = []
                    if dhcp.options is not None:
                        for opt in dhcp.options:
                            dhcp_opt.append(self.__load_core_network_dhcpop_opt(opt))

                    # add route info to data
                    val = {'id': str(dhcp.id),
                           'vcn_id': self.get_value(dhcp.vcn_id),
                           'name': self.get_value(dhcp.display_name),
                           'time_created': self.get_value(dhcp.time_created),
                           'options': dhcp_opt,
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'defined_tags': [] if dhcp.defined_tags is None else dhcp.defined_tags,
                           'freeform_tags': [] if dhcp.freeform_tags is None else dhcp.freeform_tags,
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_dhcpop", e, compartment)
            return data

    ##########################################################################
    # __load_core_network_port_range
    ##########################################################################
    def __load_core_network_seclst_rule_port_range(self, name, port_range):

        if port_range is None:
            return name + "(ALL) "

        if port_range.min == port_range.max:
            return name + "(" + str(port_range.min) + ") "
        else:
            return name + "(" + str(port_range.min) + "-" + str(port_range.max) + ") "

    ##########################################################################
    # get Network vcn security rule
    ##########################################################################
    def __load_core_network_seclst_rule(self, direction, security_rule):

        protocol_name = self.__load_core_network_seclst_protocl_name(str(security_rule.protocol))
        value = {
            'is_stateless': str(security_rule.is_stateless),
            'protocol': str(security_rule.protocol),
            'protocol_name': protocol_name,
            'source': "",
            'src_port_min': "",
            'src_port_max': "",
            'destination': "",
            'dst_port_min': "",
            'dst_port_max': "",
            'icmp_code': "",
            'icmp_type': "",
            'direction': direction,
            'security_alert': False
        }

        # Process the security rule
        line = str(direction).ljust(7) + ": "

        # process the source or dest
        if isinstance(security_rule, oci.core.models.EgressSecurityRule):
            line += "Dst: " + str(security_rule.destination).ljust(18)
            value['destination'] = str(security_rule.destination)

        if isinstance(security_rule, oci.core.models.IngressSecurityRule):
            line += "Src: " + str(security_rule.source).ljust(18)
            value['source'] = str(security_rule.source)

        # protocol
        line += str(protocol_name).ljust(6)

        # tcp options
        if security_rule.tcp_options is not None:
            line += self.__load_core_network_seclst_rule_port_range("Src", security_rule.tcp_options.source_port_range)
            line += self.__load_core_network_seclst_rule_port_range("Dst", security_rule.tcp_options.destination_port_range)

            # Handle source_port_range
            if security_rule.tcp_options.source_port_range is None:
                value['src_port_min'] = "ALL"
                value['src_port_max'] = "ALL"
            else:
                value['src_port_min'] = str(security_rule.tcp_options.source_port_range.min)
                value['src_port_max'] = str(security_rule.tcp_options.source_port_range.max)

            # Handle destination_port_range
            if security_rule.tcp_options.destination_port_range is None:
                value['dst_port_min'] = "ALL"
                value['dst_port_max'] = "ALL"
            else:
                value['dst_port_min'] = str(security_rule.tcp_options.destination_port_range.min)
                value['dst_port_max'] = str(security_rule.tcp_options.destination_port_range.max)

        # udp options
        if security_rule.udp_options is not None:
            line += self.__load_core_network_seclst_rule_port_range("Src", security_rule.udp_options.source_port_range)
            line += self.__load_core_network_seclst_rule_port_range("Dst", security_rule.udp_options.destination_port_range)

            # Handle source_port_range
            if security_rule.udp_options.source_port_range is None:
                value['src_port_min'] = "ALL"
                value['src_port_max'] = "ALL"
            else:
                value['src_port_min'] = str(security_rule.udp_options.source_port_range.min)
                value['src_port_max'] = str(security_rule.udp_options.source_port_range.max)

            # Handle destination_port_range
            if security_rule.udp_options.destination_port_range is None:
                value['dst_port_min'] = "ALL"
                value['dst_port_max'] = "ALL"
            else:
                value['dst_port_min'] = str(security_rule.udp_options.destination_port_range.min)
                value['dst_port_max'] = str(security_rule.udp_options.destination_port_range.max)

        # icmp options
        if security_rule.icmp_options is None:
            if protocol_name == "ICMP":
                value['icmp_code'] = "ALL"
                value['icmp_type'] = "ALL"
                line += "(ALL)"
        else:
            icmp = security_rule.icmp_options
            line += ""
            if icmp.code is None:
                line += "(ALL),"
                value['icmp_code'] = "ALL"
            else:
                line += str(icmp.code) + ","
                value['icmp_code'] = str(icmp.code)

            if icmp.type is None:
                line += "(ALL),"
                value['icmp_type'] = "ALL"
            else:
                line += str(icmp.type)
                value['icmp_type'] = str(icmp.type)

        # Stateless
        if security_rule.is_stateless:
            line += " (Stateless) "

        # Check security_alert
        value['security_alert'] = self.__load_core_network_check_security_alert(value)
        if value['security_alert']:
            line += " *** Security Alert *** "

        value['desc'] = line
        return value

    ##########################################################################
    # protocol name
    ##########################################################################
    def __load_core_network_seclst_protocl_name(self, protocol):

        try:
            protocol_name = ""
            if str(protocol) == "1":
                protocol_name = "ICMP"
            elif str(protocol) == "6":
                protocol_name = "TCP"
            elif str(protocol) == "17":
                protocol_name = "UDP"
            elif str(protocol) == "all" or str(protocol) == "":
                protocol_name = "ALL"
            else:
                protocol_name = str("Prot(" + str(protocol) + ")")

            return protocol_name

        except Exception as e:
            self.__print_error("__load_core_network_seclst_protocl_name", e)
            return str(protocol)

    ##########################################################################
    # data network read security list
    ##########################################################################
    def __load_core_network_seclst(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Security Lists"
            self.__load_print_status_with_threads(header)

            # Loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                sec_lists = []
                try:
                    sec_lists = oci.pagination.list_call_get_all_results(
                        virtual_network.list_security_lists,
                        compartment['id'],
                        lifecycle_state=oci.core.models.SecurityList.LIFECYCLE_STATE_AVAILABLE,
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # loop on the sec lists
                # sl = oci.core.models.SecurityList
                for sl in sec_lists:

                    # Sec Rules analyzer
                    sec_rules = []

                    for sli in sl.ingress_security_rules:
                        sec_rules.append(self.__load_core_network_seclst_rule("Ingress", sli))

                    for sle in sl.egress_security_rules:
                        sec_rules.append(self.__load_core_network_seclst_rule("Egress", sle))

                    # Add info
                    val = {'id': str(sl.id), 'vcn_id': str(sl.vcn_id), 'name': str(sl.display_name),
                           'time_created': str(sl.time_created),
                           'sec_rules': sec_rules,
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if sl.defined_tags is None else sl.defined_tags,
                           'freeform_tags': [] if sl.freeform_tags is None else sl.freeform_tags,
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_seclst", e, compartment)
            return data

    ##########################################################################
    # Return NSG names strings from NSG OCIds
    ##########################################################################
    def __load_core_network_get_nsg_names(self, nsg_ids):

        return_value = ""
        try:

            # search the nsgs, if cannot find specify the ocids instead of name
            for nsg in nsg_ids:
                result = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_NSG, 'id', str(nsg))
                if result:
                    if return_value:
                        return_value += ", "
                    return_value += result['name']
                else:
                    if return_value:
                        return_value += ", "
                    return_value += str(nsg)

            # return the value
            return return_value

        except Exception as e:
            self.__print_error("__load_core_network_get_nsg_names", e)
            return return_value

    ##########################################################################
    # get Network vcn security rule for NSG
    ##########################################################################
    def __load_core_network_nsg_secrule(self, security_rule):

        line = ""
        protocol_name = self.__load_core_network_seclst_protocl_name(str(security_rule.protocol))
        value = {
            'id': str(security_rule.id),
            'description': self.get_value(security_rule.description),
            'direction': self.get_value(security_rule.direction),
            'destination': self.get_value(security_rule.destination),
            'destination_name': "",
            'destination_type': self.get_value(security_rule.destination_type),
            'source': self.get_value(security_rule.source),
            'source_name': "",
            'source_type': self.get_value(security_rule.source_type),
            'is_stateless': ("False" if security_rule.is_stateless is None else str(security_rule.is_stateless)),
            'is_valid': self.get_value(security_rule.is_valid),
            'protocol': self.get_value(security_rule.protocol),
            'protocol_name': protocol_name,
            'time_created': self.get_value(security_rule.time_created),
            'src_port_min': "",
            'src_port_max': "",
            'dst_port_min': "",
            'dst_port_max': "",
            'icmp_code': "",
            'icmp_type': "",
            'security_alert': False
        }

        # process the source or dest
        if str(security_rule.direction) == oci.core.models.SecurityRule.DIRECTION_EGRESS:
            if security_rule.destination_type == oci.core.models.SecurityRule.DESTINATION_TYPE_NETWORK_SECURITY_GROUP:
                line = "Egress  : NSG: " + self.C_NETWORK_NSG_REPTEXT + " "
            else:
                line = "Egress  : Dst: " + str(security_rule.destination).ljust(17) + " "

        if str(security_rule.direction) == oci.core.models.SecurityRule.DIRECTION_INGRESS:
            if security_rule.source_type == oci.core.models.SecurityRule.SOURCE_TYPE_NETWORK_SECURITY_GROUP:
                line += "Ingress : NSG: " + self.C_NETWORK_NSG_REPTEXT + " "
            else:
                line += "Ingress : Src: " + str(security_rule.source).ljust(17) + " "

        # protocol
        line += str(protocol_name).ljust(6)

        # tcp options
        if security_rule.tcp_options is not None:
            line += self.__load_core_network_seclst_rule_port_range("Src", security_rule.tcp_options.source_port_range)
            line += self.__load_core_network_seclst_rule_port_range("Dst", security_rule.tcp_options.destination_port_range)

            # Handle source_port_range
            if security_rule.tcp_options.source_port_range is None:
                value['src_port_min'] = "ALL"
                value['src_port_max'] = "ALL"
            else:
                value['src_port_min'] = str(security_rule.tcp_options.source_port_range.min)
                value['src_port_max'] = str(security_rule.tcp_options.source_port_range.max)

            # Handle destination_port_range
            if security_rule.tcp_options.destination_port_range is None:
                value['dst_port_min'] = "ALL"
                value['dst_port_max'] = "ALL"
            else:
                value['dst_port_min'] = str(security_rule.tcp_options.destination_port_range.min)
                value['dst_port_max'] = str(security_rule.tcp_options.destination_port_range.max)

        # udp options
        if security_rule.udp_options is not None:
            line += self.__load_core_network_seclst_rule_port_range("Src", security_rule.udp_options.source_port_range)
            line += self.__load_core_network_seclst_rule_port_range("Dst", security_rule.udp_options.destination_port_range)

            # Handle source_port_range
            if security_rule.udp_options.source_port_range is None:
                value['src_port_min'] = "ALL"
                value['src_port_max'] = "ALL"
            else:
                value['src_port_min'] = str(security_rule.udp_options.source_port_range.min)
                value['src_port_max'] = str(security_rule.udp_options.source_port_range.max)

            # Handle destination_port_range
            if security_rule.udp_options.destination_port_range is None:
                value['dst_port_min'] = "ALL"
                value['dst_port_max'] = "ALL"
            else:
                value['dst_port_min'] = str(security_rule.udp_options.destination_port_range.min)
                value['dst_port_max'] = str(security_rule.udp_options.destination_port_range.max)

        # icmp options
        if security_rule.icmp_options is None:
            if protocol_name == "ICMP":
                value['icmp_code'] = "ALL"
                value['icmp_type'] = "ALL"
                line += "(ALL)"
        else:
            icmp = security_rule.icmp_options
            line += ""
            if icmp.code is None:
                line += "(ALL),"
                value['icmp_code'] = "ALL"
            else:
                line += str(icmp.code) + ","
                value['icmp_code'] = str(icmp.code)

            if icmp.type is None:
                line += "(ALL),"
                value['icmp_type'] = "ALL"
            else:
                line += str(icmp.type)
                value['icmp_type'] = str(icmp.type)

        # Stateless
        if security_rule.is_stateless:
            line += " (Stateless) "

        # Check security_alert
        value['security_alert'] = self.__load_core_network_check_security_alert(value)
        if value['security_alert']:
            line += " *** Security Alert *** "

        value['desc'] = line
        return value

    ##########################################################################
    # check Security Alert
    # if source = 0.0.0.0/0 and ports are not 22,443,3389
    ##########################################################################
    def __load_core_network_check_security_alert(self, security_row):
        if (
                security_row['source'] == "0.0.0.0/0" and
                security_row['protocol_name'] == "TCP" and
                not (security_row['dst_port_min'] == "22" and security_row['dst_port_max'] == "22") and
                not (security_row['dst_port_min'] == "443" and security_row['dst_port_max'] == "443") and
                not (security_row['dst_port_min'] == "3389" and security_row['dst_port_max'] == "3389")
        ):
            return True
        else:
            return False

    ##########################################################################
    # data network security groups
    ##########################################################################
    def __load_core_network_nsg(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Network Security Groups"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # ngw will throw error if run on Paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_network_security_groups,
                        compartment_id=compartment['id'],
                        lifecycle_state=oci.core.models.NetworkSecurityGroup.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning("n", False, to_print=self.flags.skip_threads)
                        errstr += "n"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.NetworkSecurityGroup
                for arr in arrs:
                    val = {'id': str(arr.id),
                           'name': self.get_value(arr.display_name),
                           'vcn_id': self.get_value(arr.vcn_id),
                           'time_created': self.get_value(arr.time_created),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region']),
                           'sec_rules': []
                           }

                    # loop on NSG
                    arrsecs = []
                    try:
                        arrsecs = oci.pagination.list_call_get_all_results(
                            virtual_network.list_network_security_group_security_rules,
                            arr.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning("p", False, to_print=self.flags.skip_threads)
                            errstr += "n"
                        else:
                            raise

                    # oci.core.models.SecurityRule
                    for arrsec in arrsecs:
                        val['sec_rules'].append(self.__load_core_network_nsg_secrule(arrsec))

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_nsg", e, compartment)
            return data

    ##########################################################################
    # data network read subnets
    ##########################################################################
    def __load_core_network_subnet(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Subnets"
            self.__load_print_status_with_threads(header)

            # Loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                subnets = []
                try:
                    subnets = oci.pagination.list_call_get_all_results(
                        virtual_network.list_subnets,
                        compartment['id'],
                        lifecycle_state=oci.core.models.Subnet.LIFECYCLE_STATE_AVAILABLE,
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # loop on the subnet
                # subnet = oci.core.models.Subnet.
                for subnet in subnets:
                    availability_domain = (str(subnet.availability_domain) if str(subnet.availability_domain) != "None" else "Regional")

                    val = {'id': str(subnet.id),
                           'vcn_id': str(subnet.vcn_id),
                           'vcn_name': "",
                           'vcn_cidr': "",
                           'vcn_domain_name': "",
                           'dns': "",
                           'name': str(subnet.display_name),
                           'cidr_block': self.get_value(subnet.cidr_block),
                           'subnet': (str(subnet.cidr_block) + "  " + availability_domain + (" (Private) " if subnet.prohibit_public_ip_on_vnic else " (Public)")),
                           'availability_domain': availability_domain,
                           'public_private': ("Private" if subnet.prohibit_public_ip_on_vnic else "Public"),
                           'time_created': self.get_value(subnet.time_created),
                           'security_list_ids': [str(es) for es in subnet.security_list_ids],
                           'dhcp_options_id': self.get_value(subnet.dhcp_options_id),
                           'route_table_id': self.get_value(subnet.route_table_id),
                           'dns_label': self.get_value(subnet.dns_label),
                           'defined_tags': [] if subnet.defined_tags is None else subnet.defined_tags,
                           'freeform_tags': [] if subnet.freeform_tags is None else subnet.freeform_tags,
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'region_name': str(self.config['region'])
                           }

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_slist", e, compartment)
            return data

    ##########################################################################
    # data network read private ip for subnet
    ##########################################################################
    def __load_core_network_subnet_add_vcn_info(self):
        try:
            if self.C_NETWORK not in self.data:
                return
            if self.C_NETWORK_SUBNET not in self.data[self.C_NETWORK] or self.C_NETWORK_VCN not in self.data[self.C_NETWORK]:
                return

            # loop on all subnets without vcn info
            for subnet in self.data[self.C_NETWORK][self.C_NETWORK_SUBNET]:
                if subnet['vcn_name']:
                    continue

                # find vcn
                for vcn in self.data[self.C_NETWORK][self.C_NETWORK_VCN]:
                    if subnet['vcn_id'] == vcn['id']:
                        subnet['dns'] = subnet['dns_label'] + "." + vcn['vcn_domain_name']
                        subnet['vcn_name'] = vcn['display_name']
                        subnet['vcn_domain_name'] = vcn['vcn_domain_name']
                        subnet['vcn_cidr'] = str(', '.join(x for x in vcn['cidr_blocks']))

        except Exception as e:
            self.__print_error("__load_core_network_subnet_add_vcn_info", e)

    ##########################################################################
    # data network read private ip for subnet
    ##########################################################################
    def __load_core_network_subnet_private_ip(self, virtual_network, subnets):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Subnet Private IPs"
            self.__load_print_status_with_threads(header)

            # loop on all subnets
            for subnet in subnets:

                private_ips = []
                try:
                    private_ips = oci.pagination.list_call_get_all_results(
                        virtual_network.list_private_ips,
                        subnet_id=subnet['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print("s", end="")

                # loop on private ips
                for ip in private_ips:
                    val = {
                        'id': str(ip.id),
                        'compartment_id': str(ip.compartment_id),
                        'compartment_name': '',
                        'compartment_path': '',
                        'display_name': self.get_value(ip.display_name),
                        'hostname_label': self.get_value(ip.hostname_label),
                        'ip_address': self.get_value(ip.ip_address),
                        'is_primary': self.get_value(ip.is_primary),
                        'vlan_id': self.get_value(ip.vlan_id),
                        'subnet_id': self.get_value(ip.subnet_id),
                        'time_created': self.get_value(ip.time_created)[0:16],
                        'vnic_id': self.get_value(ip.vnic_id),
                        'defined_tags': [] if ip.defined_tags is None else ip.defined_tags,
                        'freeform_tags': [] if ip.freeform_tags is None else ip.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # compartment
                    c = self.get_compartment_by_id(str(ip.compartment_id))
                    if c:
                        val['compartment_name'] = c['name']
                        val['compartment_path'] = c['path']

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_subnet_private_ip", e)
            return data

    ##########################################################################
    # data network read sgw
    ##########################################################################
    def __load_core_network_sgw(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Service Gateways"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                sgws = []
                try:
                    sgws = oci.pagination.list_call_get_all_results(
                        virtual_network.list_service_gateways,
                        compartment['id'],
                        lifecycle_state=oci.core.models.ServiceGateway.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on all sgws
                # sgw = oci.core.models.ServiceGateway
                for sgw in sgws:
                    val = {'id': str(sgw.id),
                           'vcn_id': self.get_value(sgw.vcn_id),
                           'name': self.get_value(sgw.display_name),
                           'time_created': self.get_value(sgw.time_created),
                           'block_traffic': self.get_value(sgw.block_traffic),
                           'route_table_id': self.get_value(sgw.route_table_id),
                           'services': str(', '.join(x.service_name for x in sgw.services)),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if sgw.defined_tags is None else sgw.defined_tags,
                           'freeform_tags': [] if sgw.freeform_tags is None else sgw.freeform_tags,
                           'region_name': str(self.config['region'])}

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_sgw", e, compartment)
            return data

    ##########################################################################
    # data network read sgw
    ##########################################################################
    def __load_core_network_nat(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "NAT Gateways"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                natgws = []
                try:
                    natgws = oci.pagination.list_call_get_all_results(
                        virtual_network.list_nat_gateways,
                        compartment['id'],
                        lifecycle_state=oci.core.models.NatGateway.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on all sgws
                # nat = oci.core.models.NatGateway.
                for nat in natgws:
                    val = {'id': str(nat.id), 'vcn_id': str(nat.vcn_id), 'name': str(nat.display_name) + " - " + str(nat.nat_ip),
                           'time_created': self.get_value(nat.time_created),
                           'block_traffic': self.get_value(nat.block_traffic),
                           'nat_ip': self.get_value(nat.nat_ip),
                           'display_name': str(nat.display_name),
                           'defined_tags': [] if nat.defined_tags is None else nat.defined_tags,
                           'freeform_tags': [] if nat.freeform_tags is None else nat.freeform_tags,
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']), 'region_name': str(self.config['region'])}

                    if nat.block_traffic:
                        val['name'] += " - Blocked"
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_nat", e, compartment)
            return data

    ##########################################################################
    # data network read drg attachment
    ##########################################################################
    def __load_core_network_dra(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Dynamic Routing GW Attch"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_drg_attachments,
                        compartment['id'],
                        attachment_type="ALL",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.DrgAttachment
                for arr in arrs:
                    if arr.lifecycle_state == oci.core.models.DrgAttachment.LIFECYCLE_STATE_ATTACHED:
                        val = {
                            'id': str(arr.id),
                            'vcn_id': self.get_value(arr.vcn_id),
                            'drg_id': self.get_value(arr.drg_id),
                            'time_created': self.get_value(arr.time_created),
                            'display_name': self.get_value(arr.display_name),
                            'is_cross_tenancy': self.get_value(arr.is_cross_tenancy),
                            'export_drg_route_distribution_id': self.get_value(arr.export_drg_route_distribution_id),
                            'drg_route_table_id': self.get_value(arr.drg_route_table_id),
                            'route_table_id': self.get_value(arr.route_table_id),
                            'compartment_name': str(compartment['name']),
                            'compartment_path': str(compartment['path']),
                            'compartment_id': str(compartment['id']),
                            'region_name': str(self.config['region']),
                            'ipsec_id': "",
                            'ipsec_connection_id': "",
                            'virtual_cirtcuit_id': "",
                            'rpc_id': ""
                        }

                        # Get attachment id
                        if arr.network_details:
                            if arr.network_details.type == "IPSEC_TUNNEL":
                                val['ipsec_id'] = arr.network_details.id
                                val['ipsec_connection_id'] = arr.network_details.ipsec_connection_id
                            if arr.network_details.type == "VCN":
                                val['vcn_id'] = arr.network_details.id
                                val['route_table_id'] = arr.network_details.route_table_id
                            if arr.network_details.type == "REMOTE_PEERING_CONNECTION":
                                val['rpc_id'] = arr.network_details.id
                            if arr.network_details.type == "VIRTUAL_CIRCUIT":
                                val['virtual_cirtcuit_id'] = arr.network_details.id

                        data.append(val)
                        cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_dra", e, compartment)
            return data

    ##########################################################################
    # data network read drg - 3/6/2023
    ##########################################################################
    def __load_core_network_drg(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Dynamic Routing GWs"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_drgs,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.Drg
                for arr in arrs:
                    if arr.lifecycle_state == oci.core.models.Drg.LIFECYCLE_STATE_AVAILABLE:
                        val = {'id': str(arr.id),
                               'name': str(arr.display_name),
                               'time_created': self.get_value(arr.time_created),
                               'redundancy': "",
                               'drg_route_tables': [],
                               'default_export_drg_route_distribution_id': self.get_value(arr.default_export_drg_route_distribution_id),
                               'compartment_name': str(compartment['name']),
                               'compartment_path': str(compartment['path']),
                               'compartment_id': str(compartment['id']),
                               'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                               'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                               'region_name': str(self.config['region'])
                               }

                        # get Redundancy
                        try:
                            # oci.core.models.DrgRedundancyStatus
                            redundancy = virtual_network.get_drg_redundancy_status(arr.id).data
                            if redundancy:
                                val['redundancy'] = str(redundancy.status)
                        except oci.exceptions.ServiceError as e:
                            if self.__check_service_error(e.code):
                                self.__load_print_auth_warning()

                        # DRG Route Tables
                        try:
                            # oci.core.models.DrgRedundancyStatus
                            route_tables = virtual_network.list_drg_route_tables(
                                arr.id,
                                lifecycle_state="AVAILABLE",
                                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                            ).data

                            for rt in route_tables:
                                rta = {
                                    'id': str(rt.id),
                                    'drg_id': str(arr.id),
                                    'display_name': self.get_value(rt.display_name),
                                    'time_created': self.get_value(rt.time_created),
                                    'route_rules': self.__load_core_network_drg_route_rules(virtual_network, rt.id),
                                    'import_drg_route_distribution_id': self.get_value(rt.import_drg_route_distribution_id),
                                    'is_ecmp_enabled': str(rt.is_ecmp_enabled),
                                    'defined_tags': [] if rt.defined_tags is None else rt.defined_tags,
                                    'freeform_tags': [] if rt.freeform_tags is None else rt.freeform_tags
                                }
                                val['drg_route_tables'].append(rta)
                                network = self.data[self.C_NETWORK]
                                network[self.C_NETWORK_DRG_RT].append(rta)

                        except oci.exceptions.ServiceError as e:
                            if e.code == 'NotAuthorizedOrNotFound':
                                pass
                            if self.__check_service_error(e.code):
                                pass

                        data.append(val)
                        cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_drg", e, compartment)
            return data

    ##########################################################################
    # data network read cpes - 3/6/2023
    ##########################################################################
    def __load_core_network_drg_route_rules(self, virtual_network, drg_route_id):

        data = []
        try:

            arrs = []
            try:
                arrs = oci.pagination.list_call_get_all_results(
                    virtual_network.list_drg_route_rules,
                    drg_route_id,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

            except oci.exceptions.ServiceError:
                return data

            # loop on array
            # arr = oci.core.models.DrgRouteRule
            for arr in arrs:
                val = {
                    'name': str(arr.route_type) + " - " + self.get_value(arr.destination_type) + " : " + self.get_value(arr.destination).ljust(18, ' ') + " -> " + self.get_value(arr.route_provenance),
                    'drg_route_id': drg_route_id,
                    'destination': self.get_value(arr.destination),
                    'destination_type': self.get_value(arr.destination_type),
                    'next_hop_drg_attachment_id': self.get_value(arr.next_hop_drg_attachment_id),
                    'route_type': self.get_value(arr.route_type),
                    'is_conflict': self.get_value(arr.is_conflict),
                    'is_blackhole': self.get_value(arr.is_blackhole),
                    'id': self.get_value(arr.id),
                    'route_provenance': self.get_value(arr.route_provenance)
                }

                # Get vcn name if VCN as destination
                if arr.route_provenance == "VCN":
                    drgatt = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_DRG_AT, 'id', arr.next_hop_drg_attachment_id)
                    if drgatt:
                        vcn_name = self.get_network_vcn(drgatt['vcn_id'])
                        val['name'] += " (" + vcn_name + ")"
                data.append(val)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_core_network_drg_route_rules", e)
            return data

    ##########################################################################
    # data network read cpes - 3/6/2023
    ##########################################################################
    def __load_core_network_cpe(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Customer Prem Equipments"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_cpes,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.Cpe
                for arr in arrs:
                    val = {'id': str(arr.id),
                           'name': self.get_value(arr.display_name) + " - " + self.get_value(arr.ip_address),
                           'display_name': self.get_value(arr.display_name),
                           'ip_address': self.get_value(arr.ip_address),
                           'time_created': self.get_value(arr.time_created),
                           'cpe_device_shape_id': self.get_value(arr.cpe_device_shape_id),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])
                           }
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_cpe", e, compartment)
            return data

    ##########################################################################
    # load network FW
    ##########################################################################
    def __load_core_network_firewall(self, network_firewall_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Network Firewalls"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        network_firewall_client.list_network_firewalls,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.network_firewall.models.NetworkFirewallSummary
                for arr in arrs:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    val = {'id': str(arr.id),
                           'name': str(arr.display_name) + " - " + str(arr.ipv4_address),
                           'display_name': self.get_value(arr.display_name),
                           'subnet_id': self.get_value(arr.subnet_id),
                           'subnet_name': "" if arr.subnet_id is None else self.get_network_subnet(arr.subnet_id, True),
                           'availability_domain': self.get_value(arr.availability_domain),
                           'ipv4_address': self.get_value(arr.ipv4_address),
                           'ipv6_address': self.get_value(arr.ipv6_address),
                           'network_firewall_policy_id': self.get_value(arr.network_firewall_policy_id),
                           'network_firewall_policy_name': "",
                           'time_created': self.get_value(arr.time_created),
                           'time_updated': self.get_value(arr.time_updated),
                           'lifecycle_state': self.get_value(arr.lifecycle_state),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])
                           }

                    # get name of the policy
                    nwfpolicy = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_FIREWALL_POLICY, 'id', arr.network_firewall_policy_id)
                    if nwfpolicy:
                        val['network_firewall_policy_name'] = nwfpolicy['display_name']

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_firewall", e, compartment)
            return data

    ##########################################################################
    # load network FW Policies
    ##########################################################################
    def __load_core_network_firewall_policy(self, network_firewall_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Network Firewalls Policies"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        network_firewall_client.list_network_firewall_policies,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.network_firewall.models.NetworkFirewallPolicySummary
                for arr in arrs:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    val = {'id': str(arr.id),
                           'display_name': str(arr.display_name),
                           'time_created': self.get_value(arr.time_created),
                           'time_updated': self.get_value(arr.time_updated),
                           'lifecycle_state': self.get_value(arr.lifecycle_state),
                           'compartment_id': str(compartment['id']),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'url_lists': "",
                           'mapped_secrets': "",
                           'application_lists': "",
                           'ip_address_lists': "",
                           'security_rules': "",
                           'decryption_rules': "",
                           'decryption_profiles': "",
                           'is_firewall_attached': "",
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    # retrieve more details with get
                    try:
                        nfw = network_firewall_client.get_network_firewall_policy(
                            arr.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                        # (dict(str, list[UrlPattern]))
                        val['url_lists'] = str(nfw.url_lists) if nfw.url_lists else ""

                        # (dict(str, MappedSecret))
                        val['mapped_secrets'] = str(nfw.mapped_secrets) if nfw.mapped_secrets else ""

                        # (dict(str, list[Application]))
                        val['application_lists'] = str(nfw.application_lists) if nfw.application_lists else ""

                        # (dict(str, list[str]))
                        val['ip_address_lists'] = str(nfw.ip_address_lists) if nfw.ip_address_lists else ""

                        # (list[oci.network_firewall.models.SecurityRule])
                        val['security_rules'] = str(nfw.security_rules) if nfw.security_rules else ""

                        # (list[oci.network_firewall.models.DecryptionRule])
                        val['decryption_rules'] = str(nfw.decryption_rules) if nfw.decryption_rules else ""

                        # (dict(str, DecryptionProfile))
                        val['decryption_profiles'] = str(nfw.decryption_profiles) if nfw.decryption_profiles else ""
                        val['is_firewall_attached'] = str(nfw.is_firewall_attached) if nfw.is_firewall_attached else ""

                    except Exception:
                        print("w", end="")

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_firewall_policy", e, compartment)
            return data

    ##########################################################################
    # query private ip
    ##########################################################################
    def __load_core_network_single_privateip(self, virtual_network, ip_id, return_name=True):

        try:
            if 'privateip' not in ip_id:
                return ""

            arr = virtual_network.get_private_ip(
                ip_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            if arr:
                if return_name:
                    return str(arr.ip_address) + " - " + str(arr.display_name)
                else:
                    return str(arr.ip_address)
            return ""

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                pass
            raise
        except Exception as e:
            self.__print_error("__get_core_network_privateip", e)
            return ""

    ##########################################################################
    # query vlan ip
    ##########################################################################
    def __load_core_network_single_vlan(self, virtual_network, vlan_id):

        try:
            if 'vlan' not in vlan_id:
                return ""

            arr = virtual_network.get_vlan(
                vlan_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            if arr:
                return "VLAN " + str(arr.vlan_tag) + " - " + str(arr.cidr_block).ljust(20) + " - " + str(arr.display_name)
            return ""

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                pass
            raise
        except Exception as e:
            self.__print_error("__load_core_network_single_vlan", e)
            return ""

    ##########################################################################
    # __load_core_network_privateip
    ##########################################################################
    def __load_core_network_privateip(self, virtual_network, routes):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Routed Private IPs"
            self.__load_print_status_with_threads(header)

            # loop on all routes with private ips
            for route in routes:
                for rl in route['route_rules']:
                    if 'privateip' not in rl['network_entity_id']:
                        continue

                    # get the list
                    arr = None
                    try:
                        arr = virtual_network.get_private_ip(
                            rl['network_entity_id'],
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data
                    except oci.exceptions.ServiceError as e:
                        if str(e.code) == 'NotAuthorizedOrNotFound':
                            continue
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"
                            continue
                        raise

                    if self.flags.skip_threads:
                        print("-", end="")

                    if arr is None:
                        continue

                    val = {'id': str(arr.id), 'name': str(arr.ip_address) + " - " + str(arr.display_name),
                           'time_created': self.get_value(arr.time_created),
                           'availability_domain': self.get_value(arr.availability_domain),
                           'hostname_label': self.get_value(arr.hostname_label),
                           'is_primary': self.get_value(arr.is_primary),
                           'ip_address': self.get_value(arr.ip_address),
                           'subnet_id': self.get_value(arr.subnet_id),
                           'compartment_id': self.get_value(arr.compartment_id),
                           'vnic_id': self.get_value(arr.vnic_id),
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_privateip", e)
            return data

    ##########################################################################
    # data network read fastconnect - 3/6/2023
    ##########################################################################
    def __load_core_network_vc(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            if self.EXCLUDE_VCIRCUITS in self.flags.exclude:
                return data

            errstr = ""
            header = "Virtual Circuits"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_virtual_circuits,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.VirtualCircuit
                for arr in arrs:

                    # get the cross connect mapping
                    data_cc = []
                    for cc in arr.cross_connect_mappings:
                        data_cc.append({'customer_bgp_peering_ip': str(cc.customer_bgp_peering_ip),
                                        'oracle_bgp_peering_ip': str(cc.oracle_bgp_peering_ip), 'vlan': str(cc.vlan)})

                    val = {'id': str(arr.id),
                           'name': str(arr.display_name),
                           'bandwidth_shape_name': self.get_value(arr.bandwidth_shape_name),
                           'bgp_management': self.get_value(arr.bgp_management),
                           'bgp_session_state': self.get_value(arr.bgp_session_state),
                           'bgp_ipv6_session_state': self.get_value(arr.bgp_ipv6_session_state),
                           'bgp_admin_state': self.get_value(arr.bgp_admin_state),
                           'is_bfd_enabled': self.get_value(arr.is_bfd_enabled),
                           'customer_asn': self.get_value(arr.customer_asn),
                           'gateway_id': self.get_value(arr.gateway_id),
                           'provider_service_id': self.get_value(arr.provider_service_id),
                           'provider_service_key_name': self.get_value(arr.provider_service_key_name),
                           'routing_policy': str(', '.join(x for x in arr.routing_policy)) if arr.routing_policy else "",
                           'public_prefixes': str(', '.join(x for x in arr.public_prefixes)) if arr.public_prefixes else "",
                           'region': arr.region,
                           'customer_bgp_asn': self.get_value(arr.customer_bgp_asn),
                           'drg_id': self.get_value(arr.gateway_id),
                           'lifecycle_state': self.get_value(arr.lifecycle_state),
                           'oracle_bgp_asn': self.get_value(arr.oracle_bgp_asn),
                           'provider_name': self.get_value(arr.provider_name),
                           'provider_service_name': self.get_value(arr.provider_service_name),
                           'provider_state': self.get_value(arr.provider_state),
                           'reference_comment': self.get_value(arr.reference_comment),
                           'service_type': self.get_value(arr.service_type),
                           'cross_connect_mappings': data_cc,
                           'type': self.get_value(arr.type), 'time_created': self.get_value(arr.time_created),
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'region_name': str(self.config['region']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'drg_route_table_id': "",
                           'drg_route_table': ""
                           }

                    # find Attachment for the VC
                    drg_attachment = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_DRG_AT, 'virtual_cirtcuit_id', arr.id)
                    if drg_attachment:
                        val['drg_route_table_id'] = drg_attachment['drg_route_table_id']
                        val['drg_route_table'] = self.get_network_drg_route_table(drg_attachment['drg_route_table_id'])

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_vc", e, compartment)
            return data

    ##########################################################################
    # data network read ipsec
    ##########################################################################
    def __load_core_network_ips(self, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "IPSEC tunnels"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        virtual_network.list_ip_sec_connections,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.IPSecConnection.
                for arr in arrs:
                    if arr.lifecycle_state == oci.core.models.IPSecConnection.LIFECYCLE_STATE_AVAILABLE:

                        # get tunnel info
                        # ipss = oci.core.models.IPSecConnectionTunnel
                        data_tun = []
                        try:
                            tunnels = virtual_network.list_ip_sec_connection_tunnels(arr.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                            tunnels_status = ""
                            for tunnel in tunnels:
                                tun_val = {'id': str(tunnel.id),
                                           'status': self.get_value(tunnel.status),
                                           'ike_version': self.get_value(tunnel.ike_version),
                                           'lifecycle_state': self.get_value(tunnel.lifecycle_state),
                                           'status_date': tunnel.time_status_updated.strftime("%Y-%m-%d %H:%M"),
                                           'display_name': self.get_value(tunnel.display_name),
                                           'routing': self.get_value(tunnel.routing),
                                           'cpe_ip': self.get_value(tunnel.cpe_ip),
                                           'vpn_ip': self.get_value(tunnel.vpn_ip),
                                           'time_created': self.get_value(tunnel.time_created),
                                           'oracle_can_initiate': self.get_value(tunnel.oracle_can_initiate),
                                           'nat_translation_enabled': self.get_value(tunnel.nat_translation_enabled),
                                           'dpd_mode': self.get_value(tunnel.dpd_mode),
                                           'dpd_timeout_in_sec': self.get_value(tunnel.dpd_timeout_in_sec),
                                           'bgp_info': "",
                                           'encryption_domain_config_oracle': "",
                                           'encryption_domain_config_cpe': "",
                                           'phase_one_details': {},
                                           'phase_two_details': {}}
                                if tunnels_status:
                                    tunnels_status += " "
                                tunnels_status += str(tunnel.status)

                                if tunnel.bgp_session_info:
                                    bs = tunnel.bgp_session_info
                                    tun_val['bgp_info'] = "BGP Status ".ljust(12) + " - " + str(bs.bgp_state) + ", Cust: " + str(bs.customer_interface_ip) + " (ASN = " + str(bs.customer_bgp_asn) + "), Oracle: " + str(bs.oracle_interface_ip) + " (ASN = " + str(bs.oracle_bgp_asn) + ")"

                                if tunnel.encryption_domain_config:
                                    env = tunnel.encryption_domain_config
                                    if env.oracle_traffic_selector:
                                        tun_val['encryption_domain_config_oracle'] = str(', '.join(x for x in env.oracle_traffic_selector))
                                    if env.cpe_traffic_selector:
                                        tun_val['encryption_domain_config_cpe'] = str(', '.join(x for x in env.cpe_traffic_selector))

                                if tunnel.phase_one_details:
                                    env = tunnel.phase_one_details
                                    tun_val['phase_one_details'] = {
                                        'is_custom_phase_one_config': str(env.is_custom_phase_one_config) if env.is_custom_phase_one_config else "",
                                        'lifetime': str(env.lifetime) if str(env.lifetime) else "",
                                        'remaining_lifetime': str(env.remaining_lifetime) if env.remaining_lifetime else "",
                                        'custom_authentication_algorithm': str(env.custom_authentication_algorithm) if env.custom_authentication_algorithm else "",
                                        'negotiated_authentication_algorithm': str(env.negotiated_authentication_algorithm) if env.negotiated_authentication_algorithm else "",
                                        'custom_encryption_algorithm': str(env.custom_encryption_algorithm) if env.custom_encryption_algorithm else "",
                                        'negotiated_encryption_algorithm': str(env.negotiated_encryption_algorithm) if env.negotiated_encryption_algorithm else "",
                                        'custom_dh_group': str(env.custom_dh_group) if env.custom_dh_group else "",
                                        'negotiated_dh_group': str(env.negotiated_dh_group) if env.negotiated_dh_group else "",
                                        'is_ike_established': str(env.is_ike_established) if env.is_ike_established else "",
                                        'remaining_lifetime_last_retrieved': str(env.remaining_lifetime_last_retrieved) if env.remaining_lifetime_last_retrieved else ""}

                                if tunnel.phase_two_details:
                                    env = tunnel.phase_two_details
                                    tun_val['phase_two_details'] = {
                                        'is_custom_phase_two_config': str(env.is_custom_phase_two_config) if env.is_custom_phase_two_config else "",
                                        'lifetime': str(env.lifetime) if str(env.lifetime) else "",
                                        'remaining_lifetime': str(env.remaining_lifetime) if env.remaining_lifetime else "",
                                        'custom_authentication_algorithm': str(env.custom_authentication_algorithm) if env.custom_authentication_algorithm else "",
                                        'negotiated_authentication_algorithm': str(env.negotiated_authentication_algorithm) if env.negotiated_authentication_algorithm else "",
                                        'custom_encryption_algorithm': str(env.custom_encryption_algorithm) if env.custom_encryption_algorithm else "",
                                        'negotiated_encryption_algorithm': str(env.negotiated_encryption_algorithm) if env.negotiated_encryption_algorithm else "",
                                        'dh_group': str(env.dh_group) if env.dh_group else "",
                                        'negotiated_dh_group': str(env.negotiated_dh_group) if env.negotiated_dh_group else "",
                                        'is_esp_established': str(env.negotiated_dh_group) if env.negotiated_dh_group else "",
                                        'is_pfs_enabled': str(env.is_pfs_enabled) if env.is_pfs_enabled else "",
                                        'remaining_lifetime_last_retrieved': str(env.remaining_lifetime_last_retrieved) if env.remaining_lifetime_last_retrieved else ""}

                                data_tun.append(tun_val)
                        except Exception:
                            pass

                        val = {'id': str(arr.id),
                               'name': str(arr.display_name),
                               'drg_id': str(arr.drg_id),
                               'tunnels_status': tunnels_status,
                               'cpe_local_identifier': self.get_value(arr.cpe_local_identifier),
                               'cpe_local_identifier_type': self.get_value(arr.cpe_local_identifier_type),
                               'cpe_id': self.get_value(arr.cpe_id),
                               'time_created': self.get_value(arr.time_created),
                               'compartment_name': str(compartment['name']),
                               'compartment_id': str(compartment['id']),
                               'compartment_path': str(compartment['path']),
                               'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                               'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                               'region_name': str(self.config['region']),
                               'static_routes': [str(es) for es in arr.static_routes],
                               'tunnels': data_tun,
                               'drg_route_table_id': "",
                               'drg_route_table': ""
                               }

                        # find Attachment for the IPSEC
                        drg_attachment = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_DRG_AT, 'ipsec_connection_id', arr.id)
                        if drg_attachment:
                            val['drg_route_table_id'] = drg_attachment['drg_route_table_id']
                            val['drg_route_table'] = self.get_network_drg_route_table(drg_attachment['drg_route_table_id'])

                        data.append(val)
                        cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_network_ips", e, compartment)
            return data

    ##########################################################################
    # __load_core_network_dns_resolvers
    ##########################################################################
    def __load_core_network_dns_resolvers(self, dns_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "DNS Resolvers"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        dns_client.list_resolvers,
                        compartment['id'],
                        lifecycle_state='ACTIVE',
                        sort_by="displayName",
                        scope="PRIVATE",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning()
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.dns.models.ResolverSummary
                for arrsummary in array:

                    arr = []
                    try:
                        # get the resolver model
                        arr = dns_client.get_resolver(arrsummary.id, scope="PRIVATE", retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                        continue

                    val = {'id': str(arr.id),
                           'display_name': str(arr.display_name),
                           'vcn_id': str(arr.attached_vcn_id),
                           'vcn_name': self.get_network_vcn(arr.attached_vcn_id),
                           'time_created': str(arr.time_created),
                           'time_updated': str(arr.time_updated),
                           'default_view_id': str(arr.default_view_id),
                           'is_protected': arr.is_protected,
                           'endpoints': [],
                           'rules': [],
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    # endpoints
                    for ep in arr.endpoints:
                        epval = {
                            'name': str(ep.name),
                            'endpoint_type': str(ep.endpoint_type),
                            'forwarding_address': str(ep.forwarding_address) if ep.forwarding_address else "",
                            'is_forwarding': ep.is_forwarding,
                            'is_listening': ep.is_listening,
                            'listening_address': str(ep.listening_address) if ep.listening_address else "",
                            'time_created': str(ep.time_created),
                            'time_updated': str(ep.time_updated)
                        }
                        val['endpoints'].append(epval)

                    # rules
                    for ep in arr.rules:
                        if ep.action == "FORWARD":
                            epval = {
                                'client_address_conditions': str(', '.join(x for x in ep.client_address_conditions)),
                                'qname_cover_conditions': str(', '.join(x for x in ep.qname_cover_conditions)),
                                'destination_addresses': str(', '.join(x for x in ep.destination_addresses)),
                                'source_endpoint_name': str(ep.source_endpoint_name),
                                'action': "FORWARD"
                            }
                        else:
                            epval = {
                                'client_address_conditions': str(', '.join(x for x in ep.client_address_conditions)),
                                'qname_cover_conditions': str(', '.join(x for x in ep.qname_cover_conditions)),
                                'action': str(ep.action)
                            }
                        val['rules'].append(epval)

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_core_network_dns_resolvers", e, compartment)
            return data

    ##########################################################################
    # __load_core_compute_main
    ##########################################################################
    def __load_section_core_compute_main(self):

        try:
            section_start_time = time.time()
            print("Compute, Block Storage and Clusters (OKE)...")

            # BlockstorageClient
            block_storage = oci.core.BlockstorageClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            compute_manage = oci.core.ComputeManagementClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            compute_client = oci.core.ComputeClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            plugin_client = oci.compute_instance_agent.PluginClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            virtual_network = oci.core.VirtualNetworkClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            auto_scaling = oci.autoscaling.AutoScalingClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            container_client = oci.container_engine.ContainerEngineClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                block_storage.base_client.session.proxies = {'https': self.flags.proxy}
                compute_manage.base_client.session.proxies = {'https': self.flags.proxy}
                compute_client.base_client.session.proxies = {'https': self.flags.proxy}
                plugin_client.base_client.session.proxies = {'https': self.flags.proxy}
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}
                auto_scaling.base_client.session.proxies = {'https': self.flags.proxy}
                container_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key to the network if not exists
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_INST)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_IMAGES)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_BOOT_VOL_ATTACH)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_VOLUME_ATTACH)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_VNIC_ATTACH)

            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_INST_CONFIG)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_INST_POOL)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_AUTOSCALING)
            self.__initialize_data_key(self.C_COMPUTE, self.C_COMPUTE_CAPACITY_RESERVATION)

            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_VOLGRP)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_BOOT)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_BOOTBACK)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_VOL)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_VOLBACK)
            self.__initialize_data_key(self.C_BLOCK, self.C_BLOCK_VOLGRPBACK)

            self.__initialize_data_key(self.C_CONTAINER, self.C_CONTAINER_CLUSTERS)
            self.__initialize_data_key(self.C_CONTAINER, self.C_CONTAINER_NODE_POOLS)

            # reference to compute
            compute = self.data[self.C_COMPUTE]
            block = self.data[self.C_BLOCK]
            cp = self.data[self.C_CONTAINER]

            ##########################
            # if serial execution
            ##########################
            if self.flags.skip_threads:
                compute[self.C_COMPUTE_INST] += self.__load_core_compute_instances(compute_client, compartments, plugin_client)
                compute[self.C_COMPUTE_IMAGES] += self.__load_core_compute_images(compute_client, compartments)
                compute[self.C_COMPUTE_BOOT_VOL_ATTACH] += self.__load_core_compute_boot_vol_attach(compute_client, compartments)
                compute[self.C_COMPUTE_VOLUME_ATTACH] += self.__load_core_compute_vol_attach(compute_client, compartments)
                compute[self.C_COMPUTE_VNIC_ATTACH] += self.__load_core_compute_vnic_attach(compute_client, virtual_network, compartments)
                compute[self.C_COMPUTE_INST_CONFIG] += self.__load_core_compute_inst_config(compute_client, compute_manage, block_storage, compartments)
                compute[self.C_COMPUTE_CAPACITY_RESERVATION] += self.__load_core_compute_capacity_reservation(compute_client, compartments)
                compute[self.C_COMPUTE_INST_POOL] += self.__load_core_compute_inst_pool(compute_manage, compartments)
                compute[self.C_COMPUTE_AUTOSCALING] += self.__load_core_compute_autoscaling(auto_scaling, compute_manage, compartments)

                block[self.C_BLOCK_VOLGRP] += self.__load_core_block_volume_group(block_storage, compartments)
                block[self.C_BLOCK_BOOT] += self.__load_core_block_boot(block_storage, compartments)
                block[self.C_BLOCK_VOL] += self.__load_core_block_volume(block_storage, compartments)

                if not self.flags.skip_backups:
                    block[self.C_BLOCK_BOOTBACK] += self.__load_core_block_boot_backup(block_storage, compartments)
                    block[self.C_BLOCK_VOLBACK] += self.__load_core_block_volume_backup(block_storage, compartments)
                    block[self.C_BLOCK_VOLGRPBACK] += self.__load_core_block_volume_group_backup(block_storage, compartments)

                cp[self.C_CONTAINER_CLUSTERS] += self.__load_container_clusters(container_client, compartments)
                cp[self.C_CONTAINER_NODE_POOLS] += self.__load_container_node_pools(container_client, compartments)

            ##########################
            # if parallel execution
            ##########################
            else:
                with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:

                    future_BLOCK_VOLGRP = executor.submit(self.__load_core_block_volume_group, block_storage, compartments)
                    future_BLOCK_BOOT = executor.submit(self.__load_core_block_boot, block_storage, compartments)
                    future_BLOCK_VOL = executor.submit(self.__load_core_block_volume, block_storage, compartments)

                    future_COMPUTE_INST = executor.submit(self.__load_core_compute_instances, compute_client, compartments, plugin_client)
                    future_COMPUTE_IMAGES = executor.submit(self.__load_core_compute_images, compute_client, compartments)
                    future_COMPUTE_BOOT_VOL_ATTACH = executor.submit(self.__load_core_compute_boot_vol_attach, compute_client, compartments)
                    future_COMPUTE_VOLUME_ATTACH = executor.submit(self.__load_core_compute_vol_attach, compute_client, compartments)
                    future_COMPUTE_VNIC_ATTACH = executor.submit(self.__load_core_compute_vnic_attach, compute_client, virtual_network, compartments)
                    future_COMPUTE_INST_CONFIG = executor.submit(self.__load_core_compute_inst_config, compute_client, compute_manage, block_storage, compartments)
                    future_COMPUTE_CAPACITY_RESERVATION = executor.submit(self.__load_core_compute_capacity_reservation, compute_client, compartments)
                    future_COMPUTE_INST_POOL = executor.submit(self.__load_core_compute_inst_pool, compute_manage, compartments)
                    future_COMPUTE_AUTOSCALING = executor.submit(self.__load_core_compute_autoscaling, auto_scaling, compute_manage, compartments)

                    future_CONTAINER_CLUSTERS = executor.submit(self.__load_container_clusters, container_client, compartments)
                    future_CONTAINER_NODE_POOLS = executor.submit(self.__load_container_node_pools, container_client, compartments)

                    # wait for main block to complete before running backups
                    block[self.C_BLOCK_VOLGRP] += next(as_completed([future_BLOCK_VOLGRP])).result()
                    block[self.C_BLOCK_BOOT] += next(as_completed([future_BLOCK_BOOT])).result()
                    block[self.C_BLOCK_VOL] += next(as_completed([future_BLOCK_VOL])).result()

                    # backup is dependent on block info
                    if not self.flags.skip_backups:
                        future_BLOCK_BOOTBACK = executor.submit(self.__load_core_block_boot_backup, block_storage, compartments)
                        future_BLOCK_VOLBACK = executor.submit(self.__load_core_block_volume_backup, block_storage, compartments)
                        future_BLOCK_VOLGRPBACK = executor.submit(self.__load_core_block_volume_group_backup, block_storage, compartments)
                        block[self.C_BLOCK_BOOTBACK] += next(as_completed([future_BLOCK_BOOTBACK])).result()
                        block[self.C_BLOCK_VOLBACK] += next(as_completed([future_BLOCK_VOLBACK])).result()
                        block[self.C_BLOCK_VOLGRPBACK] += next(as_completed([future_BLOCK_VOLGRPBACK])).result()

                    compute[self.C_COMPUTE_INST] += next(as_completed([future_COMPUTE_INST])).result()
                    compute[self.C_COMPUTE_IMAGES] += next(as_completed([future_COMPUTE_IMAGES])).result()
                    compute[self.C_COMPUTE_BOOT_VOL_ATTACH] += next(as_completed([future_COMPUTE_BOOT_VOL_ATTACH])).result()
                    compute[self.C_COMPUTE_VOLUME_ATTACH] += next(as_completed([future_COMPUTE_VOLUME_ATTACH])).result()
                    compute[self.C_COMPUTE_VNIC_ATTACH] += next(as_completed([future_COMPUTE_VNIC_ATTACH])).result()
                    compute[self.C_COMPUTE_INST_CONFIG] += next(as_completed([future_COMPUTE_INST_CONFIG])).result()
                    compute[self.C_COMPUTE_CAPACITY_RESERVATION] += next(as_completed([future_COMPUTE_CAPACITY_RESERVATION])).result()
                    compute[self.C_COMPUTE_INST_POOL] += next(as_completed([future_COMPUTE_INST_POOL])).result()
                    compute[self.C_COMPUTE_AUTOSCALING] += next(as_completed([future_COMPUTE_AUTOSCALING])).result()

                    cp[self.C_CONTAINER_CLUSTERS] += next(as_completed([future_CONTAINER_CLUSTERS])).result()
                    cp[self.C_CONTAINER_NODE_POOLS] += next(as_completed([future_CONTAINER_NODE_POOLS])).result()

            self.__load_print_section_time(section_start_time)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                print("")
                pass
            raise
        except Exception as e:
            self.__print_error("__load_section_core_compute_main", e)

    ##########################################################################
    # data compute read instances
    ##########################################################################
    def __load_core_compute_instances(self, compute, compartments, plugin_client):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Instances"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # read instances and console connections
                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        compute.list_instances,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.Instance
                for arr in arrs:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    # load data
                    val = {
                        'id': str(arr.id),
                        'display_name': self.get_value(arr.display_name),
                        'shape': self.get_value(arr.shape),
                        'lifecycle_state': self.get_value(arr.lifecycle_state),
                        'availability_domain': self.get_value(arr.availability_domain),
                        'fault_domain': self.get_value(arr.fault_domain),
                        'time_created': self.get_value(arr.time_created),
                        'time_maintenance_reboot_due': self.get_value(arr.time_maintenance_reboot_due),
                        'image_id': self.get_value(arr.image_id),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region']),
                        'console_id': "", 'console': "", 'console_connection_string': "",
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'shape_ocpu': 0,
                        'shape_memory_gb': 0,
                        'shape_storage_tb': 0,
                        'shape_gpu_description': "",
                        'shape_gpus': 0,
                        'shape_local_disk_description': "",
                        'shape_local_disks': 0,
                        'shape_max_vnic_attachments': 0,
                        'shape_networking_bandwidth_in_gbps': 0,
                        'shape_processor_description': "",
                        'shape_local_disks_total_size_in_gbs': "",
                        'shape_baseline_ocpu_utilization': "",
                        'console_vnc_connection_string': "",
                        'image': "Unknown",
                        'image_os': "Unknown",
                        'are_all_plugins_disabled': "",
                        'agent_is_management_disabled': "",
                        'agent_is_monitoring_disabled': "",
                        'agent_plugin_config': [],
                        'agent_plugin_status': [],
                        'metadata': arr.metadata,
                        'is_live_migration_preferred': "",
                        'recovery_action': "",
                        'launch_boot_volume_type': '',
                        'launch_firmware': '',
                        'launch_network_type': '',
                        'launch_remote_data_volume_type': '',
                        'launch_is_pv_encryption_in_transit_enabled': '',
                        'launch_is_consistent_volume_naming_enabled': '',
                        'platform_type': '',
                        'platform_is_secure_boot_enabled': '',
                        'platform_is_trusted_platform_module_enabled': '',
                        'platform_is_measured_boot_enabled': '',
                        'platform_is_memory_encryption_enabled': '',
                        'capacity_reservation_id': self.get_value(arr.capacity_reservation_id),
                        'dedicated_vm_host_id': self.get_value(arr.dedicated_vm_host_id),
                        'ipxe_script': self.get_value(arr.ipxe_script),
                        'launch_mode': self.get_value(arr.launch_mode),
                        'is_cross_numa_node': self.get_value(arr.is_cross_numa_node),
                        'extended_metadata': arr.extended_metadata}

                    if arr.launch_options:
                        val['launch_boot_volume_type'] = self.get_value(arr.launch_options.boot_volume_type)
                        val['launch_firmware'] = self.get_value(arr.launch_options.firmware)
                        val['launch_network_type'] = self.get_value(arr.launch_options.network_type)
                        val['launch_remote_data_volume_type'] = self.get_value(arr.launch_options.remote_data_volume_type)
                        val['launch_is_pv_encryption_in_transit_enabled'] = self.get_value(arr.launch_options.is_pv_encryption_in_transit_enabled)
                        val['launch_is_consistent_volume_naming_enabled'] = self.get_value(arr.launch_options.is_consistent_volume_naming_enabled)

                    if arr.instance_options:
                        val['are_legacy_imds_endpoints_disabled'] = self.get_value(arr.instance_options.are_legacy_imds_endpoints_disabled)

                    if arr.platform_config:
                        val['platform_type'] = self.get_value(arr.platform_config.type)
                        val['platform_is_secure_boot_enabled'] = self.get_value(arr.platform_config.is_secure_boot_enabled)
                        val['platform_is_trusted_platform_module_enabled'] = self.get_value(arr.platform_config.is_trusted_platform_module_enabled)
                        val['platform_is_measured_boot_enabled'] = self.get_value(arr.platform_config.is_measured_boot_enabled)
                        val['platform_is_memory_encryption_enabled'] = self.get_value(arr.platform_config.is_memory_encryption_enabled)

                    if arr.availability_config:
                        val['is_live_migration_preferred'] = self.get_value(arr.availability_config.is_live_migration_preferred)
                        val['recovery_action'] = self.get_value(arr.availability_config.recovery_action)

                    # agent_config
                    if arr.agent_config:
                        val["are_all_plugins_disabled"] = self.get_value(arr.agent_config.are_all_plugins_disabled)
                        val["agent_is_management_disabled"] = self.get_value(arr.agent_config.is_management_disabled)
                        val["agent_is_monitoring_disabled"] = self.get_value(arr.agent_config.is_monitoring_disabled)
                        plugin_config = []
                        if arr.agent_config.plugins_config:
                            for config in arr.agent_config.plugins_config:
                                plugin_config.append({'name': config.name, 'desired_state': config.desired_state})
                            val['agent_plugin_config'] = plugin_config

                    # agent_status
                    plugins = []
                    try:
                        # arr = oci.compute_instance_agent.models.InstanceAgentPluginSummary
                        plugins = plugin_client.list_instance_agent_plugins(compartment_id=arr.compartment_id, instanceagent_id=arr.id).data
                        for plugin in plugins:
                            val['agent_plugin_status'].append({'name': plugin.name, 'status': plugin.status, 'time_last_updated_utc': str(plugin.time_last_updated_utc)})

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"

                    # console
                    consoles = []
                    try:
                        consoles = oci.pagination.list_call_get_all_results(
                            compute.list_instance_console_connections,
                            compartment['id'],
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                        # check console connections enabled
                        for icc in consoles:
                            if str(icc.instance_id) == str(arr.id) and str(icc.lifecycle_state) == oci.core.models.InstanceConsoleConnection.LIFECYCLE_STATE_ACTIVE:
                                val['console_id'] = str(icc.id)
                                val['console'] = "Console Connection Active"
                                val['console_connection_string'] = icc.connection_string
                                val['console_vnc_connection_string'] = icc.vnc_connection_string

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"

                    # check if vm has shape config
                    if arr.shape_config:
                        sc = arr.shape_config
                        val['shape_storage_tb'] = sc.local_disks_total_size_in_gbs / 1000 if sc.local_disks_total_size_in_gbs else 0
                        val['shape_ocpu'] = sc.ocpus
                        val['shape_baseline_ocpu_utilization'] = self.get_value(sc.baseline_ocpu_utilization)
                        val['shape_memory_gb'] = sc.memory_in_gbs
                        val['shape_gpu_description'] = self.get_value(sc.gpu_description)
                        val['shape_gpus'] = self.get_value(sc.gpus)
                        val['shape_local_disk_description'] = self.get_value(sc.local_disk_description)
                        val['shape_local_disks'] = self.get_value(sc.local_disks)
                        val['shape_local_disks_total_size_in_gbs'] = self.get_value(sc.local_disks_total_size_in_gbs)
                        val['shape_max_vnic_attachments'] = sc.max_vnic_attachments
                        val['shape_networking_bandwidth_in_gbps'] = sc.networking_bandwidth_in_gbps
                        val['shape_processor_description'] = self.get_value(sc.processor_description)

                    # if PaaS compartment assign Paas Image
                    if self.__if_managed_paas_compartment(compartment['name']):
                        val['image_os'] = "PaaS Image"
                        val['image'] = "PaaS Image"

                    # mark reboot migration flag
                    if arr.time_maintenance_reboot_due is not None:
                        self.reboot_migration_counter += 1

                    # get image info
                    try:
                        # image = oci.core.models.Image
                        image = compute.get_image(arr.image_id).data
                        if image:
                            val['image'] = self.get_value(image.display_name)
                            val['image_os'] = self.get_value(image.operating_system)
                    except Exception:
                        pass

                    # add data to array

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_compute_instances", e, compartment)
            return data

    ##########################################################################
    # data compute read images
    ##########################################################################
    def __load_core_compute_images(self, compute, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Images"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                images = []
                try:
                    images = oci.pagination.list_call_get_all_results(
                        compute.list_images,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.core.models.Image.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # filter the array to only customer images
                arrs = [i for i in images if i.compartment_id is not None]

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.Image.
                for arr in arrs:
                    val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                           'base_image_id': str(arr.base_image_id),
                           'time_created': str(arr.time_created),
                           'operating_system': str(arr.operating_system),
                           'size_in_gbs': str(round(arr.size_in_mbs / 1024)),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'region_name': str(self.config['region']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'base_image_name': (str(compute.get_image(arr.base_image_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data.display_name) if arr.base_image_id else "")
                           }
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_compute_images", e, compartment)
            return data

    ##########################################################################
    # load_core_compute_capacity_reservation
    ##########################################################################
    def __load_core_compute_capacity_reservation(self, compute_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Capacity Reservation"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                if self.flags.skip_threads:
                    print(".", end="")

                list_reservations = []
                try:
                    list_reservations = oci.pagination.list_call_get_all_results(
                        compute_client.list_compute_capacity_reservations,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # loop on array
                for arr in list_reservations:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    values = ({
                        'id': str(arr.id),
                        'display_name': self.get_value(arr.display_name),
                        'lifecycle_state': self.get_value(arr.lifecycle_state),
                        'availability_domain': self.get_value(arr.availability_domain),
                        'is_default_reservation': self.get_value(arr.is_default_reservation),
                        'time_created': str(arr.time_created)[0:16],
                        'reserved_instance_count': arr.reserved_instance_count,
                        'used_instance_count': arr.used_instance_count,
                        'instances': [],
                        'config': [],
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])
                    })

                    # retrieve the config
                    try:
                        reservation = compute_client.get_compute_capacity_reservation(
                            capacity_reservation_id=arr.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                        config_data = []
                        for res_config in reservation.instance_reservation_configs:
                            config_data.append({
                                'fault_domain': str(res_config.fault_domain),
                                'instance_shape': str(res_config.instance_shape),
                                'reserved_count': res_config.reserved_count,
                                'used_count': res_config.used_count,
                                'ocpus': res_config.instance_shape_config.ocpus,
                                'memory_in_gbs': res_config.instance_shape_config.memory_in_gbs
                            })
                        values['config'] = config_data
                    except Exception:
                        errstr += "w"

                    # retrieve the instances
                    # oci.core.models.CapacityReservationInstanceSummary
                    try:
                        list_instances = oci.pagination.list_call_get_all_results(
                            compute_client.list_compute_capacity_reservation_instances,
                            capacity_reservation_id=arr.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                        instances_data = []
                        for inst in list_instances:
                            instances_data.append({
                                'id': str(inst.id),
                                'fault_domain': str(inst.fault_domain),
                                'shape': str(inst.shape),
                                'memory_in_gbs': inst.shape_config.memory_in_gbs,
                                'ocpus': inst.shape_config.ocpus
                            })
                        values['instances'] = instances_data
                    except Exception:
                        errstr += "w"

                    data.append(values)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_compute_capacity_reservation", e, compartment)
            return data

    ##########################################################################
    # compute auto scaling
    ##########################################################################
    def __load_core_compute_autoscaling(self, autoscaling, compute_manage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Autoscaling"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                autos = []
                try:
                    # pagination didn't work on auto scaling code
                    autos = oci.pagination.list_call_get_all_results(
                        autoscaling.list_auto_scaling_configurations,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.autoscaling.models.AutoScalingConfigurationSummary
                for auto in autos:
                    val = {'id': str(auto.id), 'display_name': str(auto.display_name),
                           'cool_down_in_seconds': str(auto.cool_down_in_seconds),
                           'is_enabled': auto.is_enabled,
                           'time_created': str(auto.time_created),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'region_name': str(self.config['region']),
                           'resource_id': "",
                           'resource_type': "",
                           'resource_name': "",
                           'policies': []
                           }

                    ###########################
                    # get the resources
                    # if resource is oci.autoscaling.models.InstancePoolResource
                    ###########################
                    if auto.resource:
                        if isinstance(auto.resource, oci.autoscaling.models.InstancePoolResource):
                            val['resource_id'] = str(auto.resource.id)
                            val['resource_type'] = str(auto.resource.type)

                            # get instance pool name
                            try:
                                pool_name = compute_manage.get_instance_pool(auto.resource.id).data.display_name
                                val['resource_name'] = str(pool_name)
                            except oci.exceptions.ServiceError as e:
                                if self.__check_service_error(e.code):
                                    self.__load_print_auth_warning("p", to_print=self.flags.skip_threads)
                                    errstr += "p"
                                else:
                                    raise

                    ##################
                    # get the policy
                    ##################
                    try:
                        policies = autoscaling.list_auto_scaling_policies(auto.id).data

                        # policy = oci.autoscaling.models.AutoScalingPolicySummary
                        for policy in policies:

                            # read the proper policy which has the capacity and rules
                            # pol = oci.autoscaling.models.AutoScalingPolicy
                            # didn't add the rules for now.
                            pol = autoscaling.get_auto_scaling_policy(auto.id, policy.id).data
                            if pol:
                                valpol = {'id': str(pol.id),
                                          'display_name': str(pol.display_name),
                                          'policy_type': str(pol.policy_type),
                                          'time_created': str(pol.time_created),
                                          'capacity_min': str(pol.capacity.min) if pol.capacity else "",
                                          'capacity_max': str(pol.capacity.max) if pol.capacity else "",
                                          'capacity_initial': str(pol.capacity.initial) if pol.capacity else "",
                                          'rules': []
                                          }

                                ##############################
                                # if policy is ThresholdPolicy
                                ##############################
                                try:
                                    if pol.policy_type == "threshold":
                                        for rule in pol.rules:
                                            if rule.action and rule.metric:
                                                valpol['rules'].append(
                                                    str(rule.action.type) + " " +
                                                    str(rule.action.value).ljust(3) + " when " +
                                                    str(rule.metric.metric_type) + " " +
                                                    str(rule.metric.threshold.operator) + " " +
                                                    str(rule.metric.threshold.value))
                                except Exception:
                                    pass

                                # add policy
                                val['policies'].append(valpol)

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning("l", to_print=self.flags.skip_threads)
                            errstr += "l"
                        else:
                            raise

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_compute_autoscaling", e, compartment)
            return data

    ##########################################################################
    # __load_core_compute_inst_config
    ##########################################################################
    def __load_core_compute_inst_config(self, compute, compute_manage, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Instance Configurations"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # cannot query ManagedCompartmentForPaaS
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                configs = []
                try:
                    configs = oci.pagination.list_call_get_all_results(
                        compute_manage.list_instance_configurations,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                # inst pool and inst config service often goes down, not marking warning
                # for inst pool and inst config
                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning("a", False, to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # config = oci.core.models.InstanceConfigurationSummary
                for config in configs:
                    val = {
                        'id': str(config.id),
                        'time_created': str(config.time_created),
                        'name': str(config.display_name),
                        'compute_shape': "",
                        'compute_source': "",
                        'compute_display_name': "",
                        'block_volumes': "",
                        'secondary_vnics': "",
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])}

                    arr = []
                    try:
                        # get info on the instance details
                        # arr = oci.core.models.InstanceConfiguration
                        arr = compute_manage.get_instance_configuration(config.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                    except oci.exceptions.ServiceError as e:
                        errstr += "Error for " + str(config.display_name)
                        if self.__check_service_error(e.code):
                            continue
                        continue

                    except Exception:
                        errstr += "Error for " + str(config.display_name)
                        continue

                    # instance_detail = oci.core.models.ComputeInstanceDetails
                    if not arr:
                        continue

                    if arr.instance_details:
                        instance_detail = arr.instance_details

                        # if instance_detail is ComputeInstanceDetails
                        if isinstance(instance_detail, oci.core.models.ComputeInstanceDetails):

                            # launch Details
                            if instance_detail.launch_details:
                                launch_details = instance_detail.launch_details

                                # check if instance is InstanceConfigurationLaunchInstanceDetails
                                if isinstance(launch_details, oci.core.models.InstanceConfigurationLaunchInstanceDetails):

                                    val['compute_shape'] = str(launch_details.shape)
                                    val['compute_display_name'] = str(launch_details.display_name)
                                    if instance_detail.block_volumes:
                                        val['block_volumes'] = str(len(instance_detail.block_volumes))
                                    if instance_detail.secondary_vnics:
                                        val['secondary_vnics'] = str(len(instance_detail.secondary_vnics))

                                    # check source details type
                                    if launch_details.source_details:
                                        source_details = launch_details.source_details

                                        # if InstanceConfigurationInstanceSourceViaImageDetails
                                        if isinstance(source_details, oci.core.models.InstanceConfigurationInstanceSourceViaImageDetails):
                                            if source_details.image_id:
                                                try:
                                                    val['compute_source'] = "Image: " + str(compute.get_image(source_details.image_id).data.display_name)
                                                except oci.exceptions.ServiceError as e:
                                                    if self.__check_service_error(e.code):
                                                        val['compute_source'] = "Image"

                                        # if InstanceConfigurationInstanceSourceViaBootVolumeDetails
                                        if isinstance(source_details, oci.core.models.InstanceConfigurationInstanceSourceViaBootVolumeDetails):
                                            if source_details.boot_volume_id:
                                                try:
                                                    bootvol = block_storage.get_boot_volume(source_details.boot_volume_id).data
                                                    if bootvol:
                                                        val['compute_source'] = "Boot Volume: " + str(bootvol.display_name)
                                                except oci.exceptions.ServiceError as e:
                                                    if self.__check_service_error(e.code):
                                                        val['compute_source'] = "Boot Volume"

                        data.append(val)
                        cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_inst_config", e, compartment)
            return data

    ##########################################################################
    # __load_core_compute_inst_pool
    ##########################################################################
    def __load_core_compute_inst_pool(self, compute_manage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Instance Pools"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # cannot query ManagedCompartmentForPaaS
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                pools = []
                try:
                    pools = oci.pagination.list_call_get_all_results(
                        compute_manage.list_instance_pools,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                # inst pool and inst config service often goes down, not marking warning
                # for inst pool and inst config
                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning("a", False, to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # config = oci.core.models.InstancePoolSummary
                for config in pools:
                    val = {'id': str(config.id), 'time_created': str(config.time_created),
                           'display_name': str(config.display_name),
                           'availability_domains': str(', '.join(str(x) for x in config.availability_domains)),
                           'lifecycle_state': str(config.lifecycle_state), 'size': str(config.size),
                           'instance_configuration_id': str(config.instance_configuration_id),
                           'instance_configuration_name': "", 'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}

                    inst_config = self.search_unique_item(self.C_COMPUTE, self.C_COMPUTE_INST_CONFIG, 'id', str(config.instance_configuration_id))
                    if inst_config:
                        val['instance_configuration_name'] = inst_config['name'] + " - " + inst_config['compute_shape']

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_compute_inst_pool", e, compartment)
            return data

    ##########################################################################
    # data compute read boot volume attached
    ##########################################################################
    def __load_core_compute_boot_vol_attach(self, compute, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Boot Volumes Attached"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                # loop on all ads
                ads = self.get_availability_domains(self.config['region'])

                for ad in ads:

                    arrs = []
                    try:
                        arrs = oci.pagination.list_call_get_all_results(
                            compute.list_boot_volume_attachments,
                            ad['name'],
                            compartment['id'],
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"
                            continue
                        raise

                    # loop on array
                    # arr = oci.core.models.BootVolumeAttachment
                    for arr in arrs:
                        val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                               'boot_volume_id': str(arr.boot_volume_id),
                               'instance_id': str(arr.instance_id),
                               'lifecycle_state': self.get_value(arr.lifecycle_state),
                               'time_created': self.get_value(arr.time_created),
                               'is_pv_encryption_in_transit_enabled': self.get_value(arr.is_pv_encryption_in_transit_enabled),
                               'encryption_in_transit_type': self.get_value(arr.encryption_in_transit_type),
                               'compartment_name': str(compartment['name']),
                               'compartment_id': str(compartment['id']),
                               'compartment_path': str(compartment['path']),
                               'region_name': str(self.config['region'])}
                        data.append(val)
                        cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_compute_boot_vol_attach", e, compartment)
            return data

    ##########################################################################
    # data compute read volume attached
    ##########################################################################
    def __load_core_compute_vol_attach(self, compute, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Volumes Attached"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        compute.list_volume_attachments,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.VolumeAttachment
                for arr in arrs:
                    val = {'id': str(arr.id),
                           'display_name': self.get_value(arr.display_name),
                           'volume_id': self.get_value(arr.volume_id),
                           'instance_id': self.get_value(arr.instance_id),
                           'lifecycle_state': self.get_value(arr.lifecycle_state),
                           'time_created': self.get_value(arr.time_created),
                           'attachment_type': self.get_value(arr.attachment_type),
                           'device': self.get_value(arr.device),
                           'is_read_only': self.get_value(arr.is_read_only),
                           'is_shareable': self.get_value(arr.is_shareable),
                           'is_pv_encryption_in_transit_enabled': self.get_value(arr.is_pv_encryption_in_transit_enabled),
                           'is_multipath': self.get_value(arr.is_multipath),
                           'iscsi_login_state': self.get_value(arr.iscsi_login_state),
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_compute_vol_attach", e, compartment)
            return data

    ##########################################################################
    # load Core Network Vnic
    ##########################################################################

    def __load_core_compute_vnic(self, virtual_network, vnic_id):
        data = {}
        try:
            if vnic_id is None:
                return {}

            # get the vnic
            vnic = virtual_network.get_vnic(vnic_id).data

            # add attributes to data
            data['private_ip'] = str(vnic.private_ip)
            data['display_name'] = (str(vnic.private_ip) + " (Prv)")
            data['public_ip'] = ""
            data['skip_source_dest_check'] = self.get_value(vnic.skip_source_dest_check)
            data['is_primary'] = self.get_value(vnic.is_primary)
            data['subnet'] = ""
            data['hostname_label'] = self.get_value(vnic.hostname_label)
            data['internal_fqdn'] = ""
            data['mac_address'] = self.get_value(vnic.mac_address)
            data['time_created'] = self.get_value(vnic.time_created)
            data['subnet_id'] = ""
            data['nsg_ids'] = [x for x in vnic.nsg_ids]
            data['nsg_names'] = self.__load_core_network_get_nsg_names(vnic.nsg_ids)
            data['vcn'] = ""

            # search the subnet
            subnet_display = ""
            subnet = self.search_unique_item(self.C_NETWORK, self.C_NETWORK_SUBNET, 'id', str(vnic.subnet_id))
            if subnet:
                data['subnet'] = subnet['name'] + " " + subnet['cidr_block']
                data['vcn'] = subnet['vcn_name'] + " " + subnet['vcn_cidr']
                data['subnet_id'] = subnet['id']
                subnet_display = ", Subnet (" + data['subnet'] + "), VCN (" + data['vcn'] + ")"
                data['internal_fqdn'] = str(vnic.hostname_label) + '.' + subnet['dns']

            # check vnic information
            if vnic.public_ip is not None:
                data['display_name'] += ", " + self.get_value(vnic.public_ip) + " (Pub)"
                data['public_ip'] = self.get_value(vnic.public_ip)

            # if source dest
            if vnic.skip_source_dest_check:
                data['display_name'] += " - Skip=Y"

            # if primary
            if vnic.is_primary:
                data['display_name'] += " - Primary "

            # subnet
            data['dbdesc'] = data['display_name']
            data['display_name'] += subnet_display

            # get all private_ip_addresses for vnic
            data['ip_addresses'] = []
            private_ip_addresses = virtual_network.list_private_ips(vnic_id=vnic_id).data
            for pip in private_ip_addresses:
                data['ip_addresses'].append({'ip_address': self.get_value(pip.ip_address), 'id': str(pip.id), 'type': "Private"})

                # get public ip assigned to the private ip
                try:
                    privdetails = oci.core.models.GetPublicIpByPrivateIpIdDetails()
                    privdetails.private_ip_id = pip.id
                    pub_ip = virtual_network.get_public_ip_by_private_ip_id(privdetails)
                    if pub_ip.status == 200:
                        data['ip_addresses'].append({'ip_address': self.get_value(pub_ip.data.ip_address), 'id': self.get_value(pub_ip.data.id), 'type': "Public"})
                except Exception:
                    pass

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_core_compute_vnic", e)

    ##########################################################################
    # data compute read volume attached
    ##########################################################################
    def __load_core_compute_vnic_attach(self, compute, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Vnics Attached"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        compute.list_vnic_attachments,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data
                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.VnicAttachment
                for arr in arrs:
                    if str(arr.lifecycle_state) != oci.core.models.VnicAttachment.LIFECYCLE_STATE_ATTACHED:
                        continue

                    val = {'id': str(arr.id),
                           'display_name': str(arr.display_name),
                           'vnic_id': self.get_value(arr.vnic_id),
                           'vnic_details': self.__load_core_compute_vnic(virtual_network, arr.vnic_id),
                           'instance_id': self.get_value(arr.instance_id),
                           'time_created': self.get_value(arr.time_created),
                           'nic_index': self.get_value(arr.nic_index),
                           'subnet_id': self.get_value(arr.subnet_id),
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'region_name': str(self.config['region'])}
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_compute_vnic_attach", e, compartment)
            return data

    ##########################################################################
    # get volume backup policy
    ##########################################################################
    def __load_core_block_volume_backup_policy(self, block_storage, volume_id):

        try:
            backupstr = ""
            backup_policy_assignments = block_storage.get_volume_backup_policy_asset_assignment(volume_id).data

            if backup_policy_assignments:
                for backup_policy_assignment in backup_policy_assignments:
                    bp = block_storage.get_volume_backup_policy(backup_policy_assignment.policy_id).data
                    if bp:
                        backupstr += self.get_value(bp.display_name) + " "
            return backupstr

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return ""
            raise
        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code) or e.code == 'InvalidParameter' or e.code == 'TooManyRequests':
                return ""
            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume_backup_policy", e)

    ##########################################################################
    # data compute read boot volume
    ##########################################################################
    def __load_core_block_boot(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Boot Volumes"
            self.__load_print_status_with_threads(header)

            # reference to volgroups
            volgroups = self.data[self.C_BLOCK][self.C_BLOCK_VOLGRP]

            # loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                # loop on all ads
                availability_domains = self.get_availability_domains(self.config['region'])
                for ad in availability_domains:

                    boot_volumes = []
                    try:
                        boot_volumes = oci.pagination.list_call_get_all_results(
                            block_storage.list_boot_volumes,
                            availability_domain=ad['name'],
                            compartment_id=compartment['id'],
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"
                            continue
                        raise

                    # loop on array
                    # arr = oci.core.models.BootVolume.
                    for arr in boot_volumes:

                        val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                               'size_in_gbs': self.get_value(arr.size_in_gbs),
                               'time_created': self.get_value(arr.time_created),
                               'kms_key_id': self.get_value(arr.kms_key_id),
                               'vpus_per_gb': self.get_value(arr.vpus_per_gb),
                               'is_hydrated': self.get_value(arr.is_hydrated),
                               'volume_group_id': self.get_value(arr.volume_group_id),
                               'volume_group_name': "",
                               'availability_domain': self.get_value(arr.availability_domain),
                               'compartment_name': str(compartment['name']),
                               'compartment_id': str(compartment['id']),
                               'compartment_path': str(compartment['path']),
                               'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                               'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                               'is_auto_tune_enabled': self.get_value(arr.is_auto_tune_enabled),
                               'auto_tuned_vpus_per_gb': self.get_value(arr.auto_tuned_vpus_per_gb),
                               'region_name': str(self.config['region']),
                               'backup_policy': self.__load_core_block_volume_backup_policy(block_storage, str(arr.id)),
                               'lifecycle_state': str(arr.lifecycle_state)}

                        # find vol group name
                        for volgrp in volgroups:
                            if str(arr.volume_group_id) == volgrp['id']:
                                val['volume_group_name'] = volgrp['display_name']

                        # check boot volume backup policy
                        data.append(val)
                        cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_block_boot", e, compartment)
            return data

    ##########################################################################
    # data compute read block volume
    ##########################################################################
    def __load_core_block_volume(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Block Volumes"
            self.__load_print_status_with_threads(header)

            # reference to volgroups
            volgroups = self.data[self.C_BLOCK][self.C_BLOCK_VOLGRP]

            # loop on all compartments
            for compartment in compartments:

                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        block_storage.list_volumes,
                        compartment_id=compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.Volume.
                for arr in arrs:

                    val = {'id': str(arr.id), 'display_name': str(arr.display_name),
                           'size_in_gbs': str(arr.size_in_gbs),
                           'time_created': str(arr.time_created),
                           'kms_key_id': str(arr.kms_key_id),
                           'volume_group_id': str(arr.volume_group_id),
                           'volume_group_name': "",
                           'availability_domain': str(arr.availability_domain),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'vpus_per_gb': self.get_value(arr.vpus_per_gb),
                           'is_hydrated': self.get_value(arr.is_hydrated),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region']),
                           'is_auto_tune_enabled': self.get_value(arr.is_auto_tune_enabled),
                           'auto_tuned_vpus_per_gb': self.get_value(arr.auto_tuned_vpus_per_gb),
                           'backup_policy': self.get_value(self.__load_core_block_volume_backup_policy(block_storage, str(arr.id))),
                           'lifecycle_state': str(arr.lifecycle_state)}

                    # find vol group name
                    for volgrp in volgroups:
                        if str(arr.volume_group_id) == volgrp['id']:
                            val['volume_group_name'] = volgrp['display_name']

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume", e, compartment)
            return data

    ##########################################################################
    # data compute read block volume group
    ##########################################################################
    def __load_core_block_volume_group(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Block Volume Groups"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                # retrieve the data from oci
                arrs = []
                try:
                    arrs = oci.pagination.list_call_get_all_results(
                        block_storage.list_volume_groups,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.core.models.VolumeGroup.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        if self.flags.skip_threads:
                            print(".", end="")
                        # don't count it as error, it is showing error on old tenancies
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.core.models.VolumeGroup.
                for arr in arrs:
                    val = {
                        'id': str(arr.id),
                        'display_name': str(arr.display_name),
                        'size_in_gbs': str(arr.size_in_gbs),
                        'time_created': str(arr.time_created),
                        'volume_ids': [str(a) for a in arr.volume_ids],
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'lifecycle_state': arr.lifecycle_state,
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])}

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume_group", e, compartment)
            return data

    ##########################################################################
    # data compute read boot volume backups
    ##########################################################################
    def __load_core_block_boot_backup(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Boot Volumes Backups"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                boot_volume_backups = []
                try:
                    boot_volume_backups = oci.pagination.list_call_get_all_results(
                        block_storage.list_boot_volume_backups,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.core.models.BootVolumeBackup.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # loop on array
                # arr = oci.core.models.BootVolumeBackup
                for arr in boot_volume_backups:
                    val = {'id': str(arr.id),
                           'volume_id': self.get_value(arr.boot_volume_id),
                           'boot_volume_id': self.get_value(arr.boot_volume_id),
                           'type': self.get_value(arr.type),
                           'source_type': self.get_value(arr.source_type),
                           'time_created': self.get_value(arr.time_created),
                           'display_name': self.get_value(arr.display_name),
                           'size_in_gbs': self.get_value(arr.size_in_gbs),
                           'kms_key_id': self.get_value(arr.kms_key_id),
                           'unique_size_in_gbs': self.get_value(arr.unique_size_in_gbs),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region']),
                           'backup_name': "Not Found",
                           'backup_lifecycle_state': "",
                           'expiration_time': str(arr.expiration_time)}

                    # add the rest

                    if val['expiration_time'] == "None":
                        val['expiration_time'] = "Keep"

                    # get the backup name
                    backup_name_arr = self.search_unique_item(self.C_BLOCK, self.C_BLOCK_BOOT, 'id',
                                                              str(arr.boot_volume_id))
                    if backup_name_arr:
                        val['backup_name'] = backup_name_arr['display_name']
                        val['backup_lifecycle_state'] = backup_name_arr['lifecycle_state']

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_block_boot_backup", e, compartment)
            return data

    ##########################################################################
    # data compute read block volume backups
    ##########################################################################
    def __load_core_block_volume_backup(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Block Volumes Backups"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                volume_backups = []
                try:
                    volume_backups = oci.pagination.list_call_get_all_results(
                        block_storage.list_volume_backups,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.core.models.VolumeBackup.LIFECYCLE_STATE_AVAILABLE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # loop on array
                # arr = oci.core.models.VolumeBackup
                for arr in volume_backups:

                    # add the rest
                    val = {'id': str(arr.id),
                           'volume_id': str(arr.volume_id),
                           'backup_name': "Not Found",
                           'type': str(arr.type),
                           'source_type': self.get_value(arr.source_type),
                           'time_created': self.get_value(arr.time_created),
                           'display_name': self.get_value(arr.display_name),
                           'size_in_gbs': self.get_value(arr.size_in_gbs),
                           'unique_size_in_gbs': self.get_value(arr.unique_size_in_gbs),
                           'kms_key_id': self.get_value(arr.kms_key_id),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region']),
                           'backup_lifecycle_state': "",
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'expiration_time': "Keep" if arr.expiration_time is None else str(arr.expiration_time)}

                    # get the backup name
                    backup_name_arr = self.search_unique_item(self.C_BLOCK, self.C_BLOCK_VOL, 'id', str(arr.volume_id))
                    if backup_name_arr:
                        val['backup_name'] = backup_name_arr['display_name']
                        val['backup_lifecycle_state'] = backup_name_arr['lifecycle_state']

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume_backup", e, compartment)
            return data

    ##########################################################################
    # data compute read block volume group backups
    ##########################################################################
    def __load_core_block_volume_group_backup(self, block_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Block Volumes Grp Backups"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                volume_backups = []
                try:
                    volume_backups = oci.pagination.list_call_get_all_results(
                        block_storage.list_volume_group_backups,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # loop on array
                # arr = oci.core.models.VolumeBackup
                for arr in volume_backups:

                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    # add the rest
                    val = {'id': str(arr.id),
                           'volume_id': str(arr.volume_group_id),
                           'backup_name': "Not Found",
                           'type': self.get_value(arr.type),
                           'source_type': self.get_value(arr.source_type),
                           'time_created': self.get_value(arr.time_created),
                           'display_name': self.get_value(arr.display_name),
                           'size_in_gbs': self.get_value(arr.size_in_gbs),
                           'unique_size_in_gbs': self.get_value(arr.unique_size_in_gbs),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region']),
                           'backup_lifecycle_state': "",
                           'kms_key_id': "",
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'expiration_time': "Keep" if arr.expiration_time is None else str(arr.expiration_time)}

                    # get the backup name
                    backup_name_arr = self.search_unique_item(self.C_BLOCK, self.C_BLOCK_VOLGRP, 'id', str(arr.volume_group_id))
                    if backup_name_arr:
                        val['backup_name'] = backup_name_arr['display_name']
                        val['backup_lifecycle_state'] = backup_name_arr['lifecycle_state']

                    # check boot volume backup policy
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_core_block_volume_group_backup", e, compartment)
            return data

    ##########################################################################
    # data load load balancers
    ##########################################################################
    def __load_load_balancers(self, load_balancer, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Load Balnacers"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                load_balancers = []
                try:
                    load_balancers = oci.pagination.list_call_get_all_results(
                        load_balancer.list_load_balancers,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        lifecycle_state=oci.load_balancer.models.LoadBalancer.LIFECYCLE_STATE_ACTIVE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.load_balancer.models.LoadBalancer
                for arr in load_balancers:

                    # get LB health
                    status = ""
                    try:
                        status = load_balancer.get_load_balancer_health(arr.id).data.status
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            pass
                        else:
                            raise

                    # add the rest
                    val = {'id': str(arr.id),
                           'shape_name': str(arr.shape_name),
                           'time_created': str(arr.time_created)[0:16],
                           'shape_min_mbps': "",
                           'shape_max_mbps': "",
                           'display_name': self.get_value(arr.display_name),
                           'is_private': self.get_value(arr.is_private),
                           'status': str(status),
                           'ip_addresses': [(self.get_value(ip.ip_address) + " - " + ("Public" if ip.is_public else "Private") + (" Reserved" if ip.reserved_ip else "")) for ip in arr.ip_addresses],
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'nsg_ids': [],
                           'nsg_names': "",
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region']),
                           'subnet_ids': [],
                           'certificates': '',
                           'ssl_cipher_suites': [],
                           'routing_policies': []}

                    # Flexible Shapes
                    if arr.shape_details:
                        val['shape_min_mbps'] = self.get_value(arr.shape_details.minimum_bandwidth_in_mbps)
                        val['shape_max_mbps'] = self.get_value(arr.shape_details.maximum_bandwidth_in_mbps)

                    # certificates
                    if arr.certificates:
                        val['certificates'] = self.__get_certificate_info(arr.certificates)

                    # subnets
                    if arr.subnet_ids:
                        val['subnet_ids'] = [str(a) for a in arr.subnet_ids]

                    # network_security_group_ids
                    if arr.network_security_group_ids:
                        val['nsg_ids'] = [str(a) for a in arr.network_security_group_ids]
                        val['nsg_names'] = self.__load_core_network_get_nsg_names(arr.network_security_group_ids)

                    # listeners
                    datalis = []
                    for listener in arr.listeners:
                        lo = arr.listeners[listener]
                        value = {'id': str(listener), 'port': self.get_value(lo.port), 'protocol': self.get_value(lo.protocol),
                                 'default_backend_set_name': self.get_value(lo.default_backend_set_name), 'ssl_configuration': ""}

                        # check ssl config
                        if lo.ssl_configuration:
                            value['ssl_configuration'] = self.get_value(lo.ssl_configuration.certificate_name)

                        # path_route_set_name
                        value['path_route_set_name'] = []
                        if lo.path_route_set_name:
                            value['path_route_set_name'] = self.get_value(lo.path_route_set_name)

                        # rule_set_names
                        value['rule_set_names'] = []
                        if lo.rule_set_names:
                            value['rule_set_names'] = [str(a) for a in lo.rule_set_names]

                        # host names
                        value['hostname_names'] = []
                        if lo.hostname_names:
                            value['hostname_names'] = [str(a) for a in lo.hostname_names]

                        # add data
                        datalis.append(value)

                    val['listeners'] = datalis

                    # Path route set
                    datapath = []
                    for prs in arr.path_route_sets:
                        pro = arr.path_route_sets[prs]

                        # get the path routes
                        array_path = []
                        if pro.path_routes is not None:
                            for path_route in pro.path_routes:
                                array_path.append({'path': str(path_route.path), 'backend_set_name': str(path_route.backend_set_name)})

                        # add the paths
                        datapath.append({'name': str(pro.name), 'path_routes': array_path})

                    val['path_route'] = datapath

                    # ssl_cipher_suites
                    data_ciphers = []
                    if arr.ssl_cipher_suites:
                        for cipher in arr.ssl_cipher_suites:
                            cdata = arr.ssl_cipher_suites[cipher]
                            data_ciphers.append(str(cdata.name) + ":" + ",".join([x + ":TLS" + self.get_cipher_tls(x) for x in cdata.ciphers]))

                    val['ssl_cipher_suites'] = data_ciphers

                    # routing_policies
                    routing_policies = []
                    if arr.routing_policies:
                        for rpolicy in arr.routing_policies:
                            cdata = arr.routing_policies[rpolicy]
                            routing_policies.append(str(rpolicy) + ":" + ",".join([str(x.name) + "." + str(x.condition) for x in cdata.rules]))

                    val['routing_policies'] = routing_policies

                    # Hostnames
                    datahosts = []
                    for hostname in arr.hostnames:
                        ho = arr.hostnames[hostname]
                        datahosts.append({'name': str(ho.name), 'desc': str(ho.name).ljust(20) + " - " + str(ho.hostname)})
                    val['hostnames'] = datahosts

                    # RuleSets
                    val['rule_sets'] = []
                    if arr.rule_sets:
                        val['rule_sets'] = self.__load_load_balancer_ruleset(arr.rule_sets)

                    # Add data
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_load_balancers", e, compartment)
            return data

    ##########################################################################
    # data load network load balancers
    ##########################################################################
    def __load_load_balancers_network(self, network_load_balancer, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Network Load Balancers"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                network_load_balancers = []
                try:
                    network_load_balancers = oci.pagination.list_call_get_all_results(
                        network_load_balancer.list_network_load_balancers,
                        compartment['id'],
                        sort_by="displayName",
                        lifecycle_state=oci.network_load_balancer.models.NetworkLoadBalancerSummary.LIFECYCLE_STATE_ACTIVE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.network_load_balancer.models.NetworkLoadBalancerSummary
                for arr in network_load_balancers:

                    # get LB health
                    status = ""
                    try:
                        status = network_load_balancer.get_network_load_balancer_health(arr.id).data.status
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            pass
                        else:
                            raise

                    # add the rest
                    val = {'id': str(arr.id),
                           'shape_name': "Network Load Balancer",
                           'display_name': str(arr.display_name),
                           'lifecycle_state': self.get_value(arr.lifecycle_state),
                           'lifecycle_details': self.get_value(arr.lifecycle_details),
                           'time_created': self.get_value(arr.time_created)[0:16],
                           'time_updated': self.get_value(arr.time_updated)[0:16],
                           'is_private': self.get_value(arr.is_private),
                           'is_preserve_source_destination': self.get_value(arr.is_preserve_source_destination),
                           'subnet_id': self.get_value(arr.subnet_id),
                           'subnet_name': "" if arr.subnet_id is None else self.get_network_subnet(arr.subnet_id, True),
                           'status': str(status),
                           'ip_addresses': [(self.get_value(ip.ip_address) + " - " + ("Public" if ip.is_public else "Private") + (" Reserved" if ip.reserved_ip else "")) for ip in arr.ip_addresses],
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'nsg_ids': [],
                           'nsg_names': "",
                           'system_tags': [] if arr.system_tags is None else arr.system_tags,
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    # network_security_group_ids
                    if arr.network_security_group_ids:
                        val['nsg_ids'] = [str(a) for a in arr.network_security_group_ids]
                        val['nsg_names'] = self.__load_core_network_get_nsg_names(arr.network_security_group_ids)

                    # listeners
                    datalis = []
                    for listener in arr.listeners:
                        lo = arr.listeners[listener]
                        value = {
                            'id': str(listener),
                            'name': str(lo.name),
                            'port': "ALL" if str(lo.port) == "0" else str(lo.port),
                            'protocol': str(lo.protocol),
                            'default_backend_set_name': str(lo.default_backend_set_name)
                        }

                        # add data
                        datalis.append(value)

                    val['listeners'] = datalis

                    # Add data
                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_network_load_balancers", e, compartment)
            return data

    ##########################################################################
    # data compute read block volume backups
    ##########################################################################
    def __load_load_balancer_ruleset(self, rule_sets):

        data = []

        try:
            for rule_name in rule_sets.keys():
                val = {}
                val['name'] = rule_name
                val['items'] = []

                # get items
                for ri in rule_sets[rule_name].items:
                    valitem = {}
                    if ri.action == oci.load_balancer.models.Rule.ACTION_ADD_HTTP_REQUEST_HEADER:
                        valitem = {'action': str(ri.action), 'header': str(ri.header), 'value': str(ri.value)}
                    elif ri.action == oci.load_balancer.models.Rule.ACTION_ADD_HTTP_RESPONSE_HEADER:
                        valitem = {'action': str(ri.action), 'header': str(ri.header)}
                    elif ri.action == oci.load_balancer.models.Rule.ACTION_ALLOW:
                        valitem = {'action': str(ri.action)}
                        if ri.conditions:
                            valitem['conditions'] = [str(item.attribute_name) + ":" + str(item.attribute_value) for item in ri.conditions]
                    elif ri.action == oci.load_balancer.models.Rule.ACTION_CONTROL_ACCESS_USING_HTTP_METHODS:
                        valitem = {'action': str(ri.action), 'allowed_methods': str(ri.allowed_methods), 'status_code': str(ri.status_code)}
                    elif ri.action == oci.load_balancer.models.Rule.ACTION_EXTEND_HTTP_RESPONSE_HEADER_VALUE:
                        valitem = {'action': str(ri.action), 'header': str(ri.header), 'prefix': str(ri.prefix), 'suffix': str(ri.suffix)}
                    elif ri.action == oci.load_balancer.models.Rule.ACTION_HTTP_HEADER:
                        valitem = {'action': str(ri.action), 'are_invalid_characters_allowed': str(ri.are_invalid_characters_allowed), 'http_large_header_size_in_kb': str(ri.http_large_header_size_in_kb)}
                    elif ri.action == oci.load_balancer.models.Rule.ACTION_REDIRECT:
                        valitem = {'action': str(ri.action), 'response_code': str(ri.response_code)}
                        if ri.conditions:
                            valitem['conditions'] = [str(item.attribute_name) + ":" + str(item.attribute_value) for item in ri.conditions]
                        valitem['redirect_host'] = str(ri.redirect_uri.host) + ":" + str(ri.redirect_uri.port)
                    elif ri.action == oci.load_balancer.models.Rule.ACTION_REMOVE_HTTP_REQUEST_HEADER:
                        valitem = {'action': str(ri.action), 'header': str(ri.header)}
                    elif ri.action == oci.load_balancer.models.Rule.ACTION_REMOVE_HTTP_RESPONSE_HEADER:
                        valitem = {'action': str(ri.action), 'header': str(ri.header)}
                    else:
                        valitem = {'action': str(ri.action)}
                    val['items'].append(valitem)

                # add the rule
                data.append(val)

            return data

        except Exception as e:
            self.__print_error("__load_load_balancer_ruleset", e)
            return data

    ##########################################################################
    # data compute read boot volume backups
    ##########################################################################
    def __load_load_balancer_backendset(self, load_balancer):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Load Balancer Backend Sets"
            self.__load_print_status_with_threads(header)

            # get the load balancers for this regions
            region_name = str(self.config['region'])
            load_balancers = self.search_multi_items(self.C_LB, self.C_LB_LOAD_BALANCERS, 'region_name', region_name)

            # loop on all load balancers
            for lb in load_balancers:
                load_balancer_id = lb['id']
                region_name = lb['region_name']

                ############################
                # get backend set and status
                ############################
                backend_sets = []
                try:
                    backend_sets = oci.pagination.list_call_get_all_results(
                        load_balancer.list_backend_sets,
                        load_balancer_id,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        self.__load_print_auth_warning("b", False, to_print=self.flags.skip_threads)
                        errstr += "b"
                        time.sleep(1)
                        continue

                # print next load balancer
                if self.flags.skip_threads:
                    print("L", end="")

                # loop on backendsets
                # bs = oci.load_balancer.models.BackendSet
                for bs in backend_sets:

                    ############################
                    # get status
                    ############################
                    status = ""
                    try:
                        status = load_balancer.get_backend_set_health(load_balancer_id, bs.name).data.status
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            pass
                        else:
                            self.__load_print_auth_warning("s", False, to_print=self.flags.skip_threads)
                            errstr += "s"
                            status = "-"
                            time.sleep(1)

                    ############################
                    # check ssl config
                    ############################
                    ssl_details = ""
                    if bs.ssl_configuration is not None:
                        ssl_details = str(bs.ssl_configuration.certificate_name)

                    # copy load balancer info
                    dataval = {'load_balancer_id': load_balancer_id,
                               'compartment_name': lb['compartment_name'],
                               'compartment_id': lb['compartment_id'],
                               'region_name': lb['region_name'],
                               'name': str(bs.name),
                               'policy': str(bs.policy),
                               'ssl_configuration': ssl_details,
                               'status': str(status),
                               'desc': str(bs.name) + " - " + str(bs.policy) + (" - cert:" + ssl_details if ssl_details else "")
                               }

                    ############################
                    # list of backends
                    ############################
                    databck = []
                    for backend in bs.backends:
                        bh_status = ""

                        # Check Status
                        try:
                            bh_status = load_balancer.get_backend_health(load_balancer_id, bs.name, backend.name).data.status
                        except oci.exceptions.ServiceError as e:
                            if self.__check_service_error(e.code):
                                pass
                            else:
                                self.__load_print_auth_warning("h", False)
                                bh_status = "-"
                                time.sleep(1)

                        # add details
                        bval = {'name': str(backend.name),
                                'status': str(bh_status),
                                'ip_address': str(backend.ip_address),
                                'port': str(backend.port),
                                'backup': str(backend.backup),
                                'drain': str(backend.drain),
                                'offline': str(backend.offline),
                                'weight': str(backend.weight),
                                'desc': (str(bh_status).ljust(4)[0:4] + " - " + str(backend.ip_address) + ":" + str(backend.port) + " - Backup=" + ("Y" if backend.backup else "N") + ", " + "Drain=" + ("Y" if backend.drain else "N") + ", " + "Offline=" + ("Y" if backend.offline else "N") + ", " + "Weight=" + str(backend.weight))
                                }
                        databck.append(bval)
                    dataval['backends'] = databck

                    # Health Checker
                    h = bs.health_checker
                    datahealth = {'protocol': str(h.protocol),
                                  'interval_in_millis': str(h.interval_in_millis),
                                  'timeout_in_millis': str(h.timeout_in_millis),
                                  'retries': str(h.retries),
                                  'port': str(h.port),
                                  'return_code': str(h.return_code),
                                  'response_body_regex': str(h.response_body_regex),
                                  'url_path': str(h.url_path)}
                    dataval['health_checker'] = datahealth

                    # session_persistence_configuration
                    dataval['session_persistence'] = ""
                    if bs.session_persistence_configuration is not None:
                        bss = bs.session_persistence_configuration
                        vallb = {
                            'cookie_name': str(bss.cookie_name),
                            'disable_fallback': str(bss.disable_fallback),
                            'desc': str(bss.cookie_name) + ", " + "disable_fallback=" + ("Y" if bss.disable_fallback else "N")
                        }
                        dataval['session_persistence'] = vallb

                    # ssl_configuration
                    dataval['ssl_cert'] = ""
                    if bs.ssl_configuration is not None:
                        bss = bs.ssl_configuration
                        vallb = {
                            'certificate_name': str(bss.certificate_name),
                            'verify_peer_certificate': str(bss.verify_peer_certificate),
                            'verify_depth': str(bss.verify_depth),
                            'desc': (str(bss.certificate_name) + ", VerifyPeer=" + ("Y" if bss.verify_peer_certificate else "N") + ", " + "VerifyDepth=" + str(bss.verify_depth))
                        }
                        dataval['ssl_cert'] = vallb

                    # lb_cookie_session_persistence_configuration
                    dataval['lb_cookie_session_persistence_configuration'] = ""
                    if bs.lb_cookie_session_persistence_configuration is not None:
                        lbc = bs.lb_cookie_session_persistence_configuration
                        vallb = {
                            'cookie_name': str(lbc.cookie_name),
                            'disable_fallback': str(lbc.disable_fallback),
                            'domain': str(lbc.domain),
                            'path': str(lbc.path),
                            'max_age_in_seconds': str(lbc.max_age_in_seconds),
                            'is_secure': str(lbc.is_secure),
                            'is_http_only': str(lbc.is_http_only),
                            'desc': (str(lbc.cookie_name) + ", " + "disable_fallback=" + ("Y" if lbc.disable_fallback else "N") + ", domain=" +
                                     ("" if str(lbc.domain) == "None" else str(lbc.domain)) +
                                     ", path=" + ("" if str(lbc.path) == "None" else str(lbc.path)) +
                                     ", age=" + ("" if str(lbc.max_age_in_seconds) == "None" else str(lbc.max_age_in_seconds)) +
                                     ", is_secure=" + ("Y" if lbc.is_secure else "N") +
                                     ", is_http_only=" + ("Y" if lbc.is_http_only else "N"))
                        }
                        dataval['lb_cookie_session_persistence_configuration'] = vallb

                    # add data
                    data.append(dataval)

                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_load_balancer_backendset", e)
            return data

    ##########################################################################
    # __load_network_load_balancer_backendset
    ##########################################################################
    def __load_load_balancer_backendset_network(self, network_load_balancer):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Network LB Backend Sets"
            self.__load_print_status_with_threads(header)

            # get the load balancers for this regions
            region_name = str(self.config['region'])
            load_balancers = self.search_multi_items(self.C_LB, self.C_LB_NETWORK_LOAD_BALANCERS, 'region_name', region_name)

            # loop on all load balancers
            for lb in load_balancers:
                load_balancer_id = lb['id']
                region_name = lb['region_name']

                ############################
                # get backend set and status
                ############################
                backend_sets = []
                try:
                    backend_sets = network_load_balancer.list_backend_sets(load_balancer_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        self.__load_print_auth_warning("b", False, to_print=self.flags.skip_threads)
                        errstr += "b"
                        time.sleep(1)
                        continue

                # print next load balancer
                if self.flags.skip_threads:
                    print("L", end="")

                # loop on backendsets
                if backend_sets:
                    for bs in backend_sets.items:

                        ############################
                        # get status
                        ############################
                        status = ""
                        try:
                            status = network_load_balancer.get_backend_set_health(load_balancer_id, bs.name).data.status
                        except oci.exceptions.ServiceError as e:
                            if self.__check_service_error(e.code):
                                pass
                            else:
                                self.__load_print_auth_warning("s", False)
                                status = "-"
                                time.sleep(1)

                        # copy load balancer info
                        dataval = {'load_balancer_id': load_balancer_id,
                                   'compartment_name': lb['compartment_name'],
                                   'compartment_id': lb['compartment_id'],
                                   'region_name': lb['region_name'],
                                   'name': str(bs.name),
                                   'policy': str(bs.policy),
                                   'status': str(status),
                                   'desc': str(bs.name) + " - " + str(bs.policy)
                                   }

                        ############################
                        # list of backends
                        ############################
                        databck = []
                        for backend in bs.backends:
                            bh_status = ""

                            # Check Status
                            try:
                                bh_status = network_load_balancer.get_backend_health(load_balancer_id, bs.name, backend.name).data.status
                            except oci.exceptions.ServiceError as e:
                                if self.__check_service_error(e.code):
                                    pass
                                else:
                                    self.__load_print_auth_warning("h", False, to_print=self.flags.skip_threads)
                                    errstr += "h"
                                    bh_status = "-"
                                    time.sleep(1)

                            # add details
                            bval = {'name': str(backend.name),
                                    'id': str(backend.name),
                                    'ip_address': str(backend.ip_address),
                                    'status': str(bh_status),
                                    'target_id': str(backend.target_id),
                                    'port': "ALL" if str(backend.port) == "0" else str(backend.port),
                                    'weight': str(backend.weight),
                                    'is_backup': str(backend.is_backup),
                                    'is_drain': str(backend.is_drain),
                                    'is_offline': str(backend.is_offline),
                                    'desc': (str(bh_status).ljust(4)[0:4] + " - " + str(backend.ip_address) + ":" + ("ALL" if str(backend.port) == "0" else str(backend.port)) + " - Backup=" + ("Y" if backend.is_backup else "N") + ", " + "Drain=" + ("Y" if backend.is_drain else "N") + ", " + "Offline=" + ("Y" if backend.is_offline else "N") + ", " + "Weight=" + str(backend.weight))
                                    }
                            databck.append(bval)
                        dataval['backends'] = databck

                        # Health Checker
                        h = bs.health_checker
                        datahealth = {'protocol': str(h.protocol),
                                      'interval_in_millis': str(h.interval_in_millis),
                                      'timeout_in_millis': str(h.timeout_in_millis),
                                      'retries': str(h.retries),
                                      'port': str(h.port),
                                      'return_code': str(h.return_code),
                                      'request_data': str(h.request_data),
                                      'response_data': str(h.response_data),
                                      'response_body_regex': str(h.response_body_regex),
                                      'url_path': str(h.url_path)}
                        dataval['health_checker'] = datahealth

                        # add data
                        data.append(dataval)

                        cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_network_load_balancer_backendset", e)
            return data

    ##########################################################################
    # __load_object_storage_file_storage_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.object_storage.ObjectStorageClient(config, **kwargs)
    #
    ##########################################################################
    def __load_section_object_storage_file_storage_main(self):

        try:
            print("Object and File Storage...")

            file_storage = oci.file_storage.FileStorageClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            object_storage = oci.object_storage.ObjectStorageClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            virtual_network = oci.core.VirtualNetworkClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                file_storage.base_client.session.proxies = {'https': self.flags.proxy}
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}
                object_storage.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_FILE_STORAGE, self.C_FILE_STORAGE_FILESYSTEMS)
            self.__initialize_data_key(self.C_FILE_STORAGE, self.C_FILE_STORAGE_EXPORTS)
            self.__initialize_data_key(self.C_FILE_STORAGE, self.C_FILE_STORAGE_MOUNTS)
            self.__initialize_data_key(self.C_OS, self.C_OS_BUCKETS)

            # reference to orm
            fs = self.data[self.C_FILE_STORAGE]
            os = self.data[self.C_OS]

            ##########################
            # if serial execution
            ##########################
            if self.flags.skip_threads:
                fs[self.C_FILE_STORAGE_FILESYSTEMS] += self.__load_file_storage_filesystems(file_storage, compartments)
                fs[self.C_FILE_STORAGE_EXPORTS] += self.__load_file_storage_exports(file_storage, compartments)
                fs[self.C_FILE_STORAGE_MOUNTS] += self.__load_file_storage_mount_targets(file_storage, virtual_network, compartments)
                os[self.C_OS_BUCKETS] += self.__load_object_storage_buckets(object_storage, compartments)

            ##########################
            # if parallel execution
            ##########################
            else:
                with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                    future_FILE_STORAGE_FILESYSTEMS = executor.submit(self.__load_file_storage_filesystems, file_storage, compartments)
                    future_FILE_STORAGE_EXPORTS = executor.submit(self.__load_file_storage_exports, file_storage, compartments)
                    future_FILE_STORAGE_MOUNTS = executor.submit(self.__load_file_storage_mount_targets, file_storage, virtual_network, compartments)
                    future_OS_BUCKETS = executor.submit(self.__load_object_storage_buckets, object_storage, compartments)

                    fs[self.C_FILE_STORAGE_FILESYSTEMS] += next(as_completed([future_FILE_STORAGE_FILESYSTEMS])).result()
                    fs[self.C_FILE_STORAGE_EXPORTS] += next(as_completed([future_FILE_STORAGE_EXPORTS])).result()
                    fs[self.C_FILE_STORAGE_MOUNTS] += next(as_completed([future_FILE_STORAGE_MOUNTS])).result()
                    os[self.C_OS_BUCKETS] += next(as_completed([future_OS_BUCKETS])).result()

            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_section_object_storage_file_storage_main", e)

    ##########################################################################
    # data load load balancers
    ##########################################################################
    def __load_object_storage_buckets(self, object_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Object Storage Buckets"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                buckets = []
                try:
                    namespace_name = object_storage.get_namespace().data
                    buckets = oci.pagination.list_call_get_all_results(
                        object_storage.list_buckets,
                        namespace_name,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning()
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on array
                # arr = oci.object_storage.models.BucketSummary
                for arr in buckets:
                    val = {
                        'name': str(arr.name),
                        'time_created': str(arr.time_created)[0:16],
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region']),
                        'namespace_name': namespace_name,
                        'storage_tier': '',
                        'archival_state': '',
                        'public_access_type': '',
                        'object_events_enabled': '',
                        'defined_tags': [],
                        'freeform_tags': [],
                        'kms_key_id': '',
                        'object_lifecycle_policy_etag': '',
                        'replication_enabled': '',
                        'is_read_only': '',
                        'versioning': '',
                        'auto_tiering': '',
                        'id': '',
                        'size_gb': "",
                        'count': "",
                        'approximate_count': "",
                        'approximate_size': "",
                        'object_lifecycle': "",
                        'preauthenticated_requests': "",
                        'error_message': ""
                    }

                    try:
                        # bucket = oci.object_storage.models.Bucket
                        bucket = object_storage.get_bucket(
                            namespace_name=namespace_name,
                            bucket_name=str(arr.name),
                            fields=['approximateCount', 'approximateSize', 'autoTiering'],
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                        if bucket:
                            val['storage_tier'] = self.get_value(bucket.storage_tier)
                            val['public_access_type'] = self.get_value(bucket.public_access_type)
                            val['object_events_enabled'] = self.get_value(bucket.object_events_enabled)
                            val['defined_tags'] = [] if bucket.defined_tags is None else bucket.defined_tags
                            val['freeform_tags'] = [] if bucket.freeform_tags is None else bucket.freeform_tags
                            val['kms_key_id'] = self.get_value(bucket.kms_key_id)
                            val['object_lifecycle_policy_etag'] = str(bucket.object_lifecycle_policy_etag)
                            val['replication_enabled'] = self.get_value(bucket.replication_enabled)
                            val['is_read_only'] = self.get_value(bucket.is_read_only)
                            val['versioning'] = self.get_value(bucket.versioning)
                            val['auto_tiering'] = self.get_value(bucket.auto_tiering)
                            val['id'] = str(bucket.id)
                            objcnt = bucket.approximate_count
                            size = bucket.approximate_size

                            # check if size if not empty
                            if objcnt is not None and size is not None:
                                val['approximate_count'] = str('{:11,.0f}'.format(objcnt))
                                val['approximate_size'] = str('{:11,.1f}'.format(round(size / 1024 / 1024 / 1024, 1)))
                                val['size_gb'] = str(round(size / 1024 / 1024 / 1024, 1))
                                val['count'] = objcnt

                    except oci.exceptions.ServiceError as e:
                        errstr += "Issue with " + arr.name + " "
                        val['error_message'] = str(e)
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)

                    except Exception as e:
                        errstr += "Issue with " + arr.name + " "
                        val['error_message'] = str(e)
                        if 'KmsKeyDisabled' in str(e):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"

                    ###############################
                    # get object lifecycle
                    ###############################
                    lp = None
                    try:
                        lp = object_storage.get_object_lifecycle_policy(namespace_name, str(arr.name)).data
                        if lp:
                            for lc in lp.items:
                                if val['object_lifecycle']:
                                    val['object_lifecycle'] += ", "
                                val['object_lifecycle'] += str(lc.name) + " - " + str(lc.action) + " - " + str(lc.time_amount) + " " + str(lc.time_unit)
                    except oci.exceptions.ServiceError as e:
                        if e.code == "LifecyclePolicyNotFound":
                            pass
                        elif self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        else:
                            raise

                    data.append(val)
                    cnt += 1

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_object_storage_buckets", e)
            return data

    ##########################################################################
    # __load_file_storage_filesystems
    ##########################################################################
    def __load_file_storage_filesystems(self, file_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "File Storage"
            self.__load_print_status_with_threads(header)

            # get availability domains
            availability_domains = self.get_availability_domains(self.config['region'])

            # loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                for ad in availability_domains:

                    file_systems = []
                    try:
                        file_systems = oci.pagination.list_call_get_all_results(
                            file_storage.list_file_systems,
                            compartment['id'], ad['name'],
                            lifecycle_state=oci.file_storage.models.FileSystemSummary.LIFECYCLE_STATE_ACTIVE,
                            sort_by="DISPLAYNAME",
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"
                            continue
                        raise

                    # query the stacks
                    # fs = oci.file_storage.models.FileSystemSummary.
                    for fs in file_systems:
                        val = {'id': str(fs.id),
                               'display_name': str(fs.display_name),
                               'time_created': self.get_value(fs.time_created)[0:16],
                               'availability_domain': self.get_value(fs.availability_domain),
                               'size_gb': str(round(int(fs.metered_bytes) / 1024 / 1024 / 1024, 1)),
                               'metered_bytes': self.get_value(fs.metered_bytes),
                               'snapshots': [],
                               'defined_tags': [] if fs.defined_tags is None else fs.defined_tags,
                               'freeform_tags': [] if fs.freeform_tags is None else fs.freeform_tags,
                               'compartment_name': str(compartment['name']),
                               'compartment_id': str(compartment['id']),
                               'compartment_path': str(compartment['path']),
                               'kms_key_id': str(fs.kms_key_id),
                               'region_name': str(self.config['region'])}

                        # add snapshots to the file systems
                        try:
                            snapshots = oci.pagination.list_call_get_all_results(
                                file_storage.list_snapshots,
                                file_system_id=str(fs.id),
                                lifecycle_state=oci.file_storage.models.SnapshotSummary.LIFECYCLE_STATE_ACTIVE,
                                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                            ).data

                            for snap in snapshots:
                                sval = {'id': str(snap.id), 'name': str(snap.name), 'time_created': str(snap.time_created)}
                                val['snapshots'].append(sval)
                        except oci.exceptions.ServiceError as e:
                            if self.__check_service_error(e.code):
                                continue
                            else:
                                raise

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_file_storage_filesystems", e)
            return data

    ##########################################################################
    # __load_file_storage_mount_targets
    ##########################################################################
    def __load_file_storage_mount_targets(self, file_storage, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "File Storage Mounts"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                # get availability domains
                availability_domains = self.get_availability_domains(self.config['region'])
                for ad in availability_domains:

                    mount_targets = []
                    try:
                        mount_targets = oci.pagination.list_call_get_all_results(
                            file_storage.list_mount_targets,
                            compartment['id'], ad['name'],
                            lifecycle_state=oci.file_storage.models.MountTargetSummary.LIFECYCLE_STATE_ACTIVE,
                            sort_by="DISPLAYNAME",
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"
                            continue
                        raise

                    # query the stacks
                    # mt = oci.file_storage.models.MountTargetSummary
                    for mt in mount_targets:
                        val = {'id': str(mt.id),
                               'display_name': self.get_value(mt.display_name),
                               'export_set_id': self.get_value(mt.export_set_id),
                               'time_created': self.get_value(mt.time_created),
                               'availability_domain': self.get_value(mt.availability_domain),
                               'private_ip_ids': [],
                               'subnet_id': self.get_value(mt.subnet_id),
                               'compartment_name': str(compartment['name']),
                               'compartment_path': str(compartment['path']),
                               'compartment_id': str(compartment['id']),
                               'region_name': str(self.config['region'])}

                        # get private ips
                        for e in mt.private_ip_ids:
                            ip_address = self.__load_core_network_single_privateip(virtual_network, e)
                            val['private_ip_ids'].append(ip_address)

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_file_storage_mount_targets", e)
            return data

    ##########################################################################
    # __load_file_storage_exports
    ##########################################################################
    def __load_file_storage_exports(self, file_storage, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "File Storage Exports"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                if self.flags.skip_threads:
                    print(".", end="")

                exports = []
                try:
                    exports = oci.pagination.list_call_get_all_results(
                        file_storage.list_exports,
                        compartment_id=compartment['id'],
                        lifecycle_state=oci.file_storage.models.ExportSummary.LIFECYCLE_STATE_ACTIVE,
                        sort_by="PATH",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                # query the export
                # es = oci.file_storage.models.ExportSummary
                for es in exports:
                    val = {'id': str(es.id),
                           'export_set_id': self.get_value(es.export_set_id),
                           'file_system_id': self.get_value(es.file_system_id),
                           'path': self.get_value(es.path),
                           'time_created': self.get_value(es.time_created),
                           'export_set': []}

                    # export set
                    try:
                        exp = file_storage.get_export_set(es.export_set_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                        if exp:
                            valexp = {'id': str(exp.id), 'compartment_id': str(exp.compartment_id),
                                      'availability_domain': str(exp.availability_domain),
                                      'display_name': self.get_value(exp.display_name),
                                      'lifecycle_state': self.get_value(exp.lifecycle_state),
                                      'max_fs_stat_bytes': self.get_value(exp.max_fs_stat_bytes),
                                      'max_fs_stat_files': self.get_value(exp.max_fs_stat_files),
                                      'time_created': str(exp.time_created),
                                      'vcn_id': self.get_value(exp.vcn_id),
                                      'options': []}
                            exp_summary = file_storage.list_exports(export_set_id=exp.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                            for e in exp_summary:
                                xport = file_storage.get_export(e.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                                opts = xport.export_options
                                for opt in opts:
                                    valexp['options'].append({
                                        'access': opt.access,
                                        'anonymous_gid': opt.anonymous_gid,
                                        'anonymous_uid': opt.anonymous_uid,
                                        'identity_squash': opt.identity_squash,
                                        'require_privileged_source_port': opt.require_privileged_source_port,
                                        'source': opt.source
                                    })
                            val['export_set'] = valexp

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            continue
                        else:
                            raise

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_file_storage_exports", e)
            return data

    ##########################################################################
    # __load_database_main
    ##########################################################################
    def __load_section_database_main(self):

        try:
            section_start_time = time.time()
            print("Database...")

            # DatabaseClient
            database_client = oci.database.DatabaseClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            virtual_network = oci.core.VirtualNetworkClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            nosql_client = oci.nosql.NosqlClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            mysql_client = oci.mysql.DbSystemClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            gg_client = oci.golden_gate.GoldenGateClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                database_client.base_client.session.proxies = {'https': self.flags.proxy}
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}
                nosql_client.base_client.session.proxies = {'https': self.flags.proxy}
                mysql_client.base_client.session.proxies = {'https': self.flags.proxy}
                gg_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_HOMES)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_BACKUPS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_DBSYSTEMS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXADATA)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXADATA_VMS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXACC)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXACC_VMS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXACC_ADB_VMS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXACC_DBSERVERS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_ADB_DATABASE)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_ADB_D_VMS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_ADB_D_CONTAINERS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_NOSQL)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_MYSQL)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_SOFTWARE_IMAGES)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_GG_DB_REGISTRATION)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_GG_DEPLOYMENTS)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXTERNAL_CDB)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXTERNAL_PDB)
            self.__initialize_data_key(self.C_DATABASE, self.C_DATABASE_EXTERNAL_NONPDB)

            # reference to orm
            db = self.data[self.C_DATABASE]

            ##########################
            # if serial execution
            ##########################
            if self.flags.skip_threads:
                db[self.C_DATABASE_BACKUPS] += self.__load_database_standalone_backups(database_client, compartments)
                db[self.C_DATABASE_HOMES] += self.__load_database_homes(database_client, compartments)
                db[self.C_DATABASE_EXACC] += self.__load_database_exacc_infrastructure(database_client, virtual_network, compartments)
                db[self.C_DATABASE_EXACC_VMS] += self.__load_database_exacc_vm_clusters(database_client, virtual_network, compartments)
                db[self.C_DATABASE_EXACC_ADB_VMS] += self.__load_database_exacc_adb_vmclusters(database_client, compartments)
                db[self.C_DATABASE_EXADATA] += self.__load_database_exadata_infrastructure(database_client, virtual_network, compartments)
                db[self.C_DATABASE_EXADATA_VMS] += self.__load_database_exadata_vm_clusters(database_client, virtual_network, compartments)
                db[self.C_DATABASE_DBSYSTEMS] += self.__load_database_dbsystems(database_client, virtual_network, compartments)
                db[self.C_DATABASE_ADB_D_VMS] += self.__load_database_adb_d_vmclusters(database_client, compartments)
                db[self.C_DATABASE_ADB_D_CONTAINERS] += self.__load_database_adb_d_containers(database_client, compartments)
                db[self.C_DATABASE_ADB_DATABASE] += self.__load_database_adb_database(database_client, compartments)
                db[self.C_DATABASE_NOSQL] += self.__load_database_nosql(nosql_client, compartments)
                db[self.C_DATABASE_MYSQL] += self.__load_database_mysql(mysql_client, compartments)
                db[self.C_DATABASE_SOFTWARE_IMAGES] += self.__load_database_software_images(database_client, compartments)
                db[self.C_DATABASE_GG_DEPLOYMENTS] += self.__load_database_gg_deployments(gg_client, compartments)
                db[self.C_DATABASE_GG_DB_REGISTRATION] += self.__load_database_gg_db_registration(gg_client, compartments)
                db[self.C_DATABASE_EXTERNAL_CDB] += self.__load_database_external_cdb(database_client, compartments)
                db[self.C_DATABASE_EXTERNAL_PDB] += self.__load_database_external_pdb(database_client, compartments)
                db[self.C_DATABASE_EXTERNAL_NONPDB] += self.__load_database_external_nonpdb(database_client, compartments)

            ##########################
            # if parallel execution
            ##########################
            else:
                with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                    future_BACKUPS = executor.submit(self.__load_database_standalone_backups, database_client, compartments)
                    future_EXACC = executor.submit(self.__load_database_exacc_infrastructure, database_client, virtual_network, compartments)
                    future_EXACC_ADB_VMS = executor.submit(self.__load_database_exacc_adb_vmclusters, database_client, compartments)
                    future_EXADATA = executor.submit(self.__load_database_exadata_infrastructure, database_client, virtual_network, compartments)
                    future_ADB_D_VMS = executor.submit(self.__load_database_adb_d_vmclusters, database_client, compartments)
                    future_ADB_D_CONTAINERS = executor.submit(self.__load_database_adb_d_containers, database_client, compartments)
                    future_ADB_DATABASE = executor.submit(self.__load_database_adb_database, database_client, compartments)
                    future_NOSQL = executor.submit(self.__load_database_nosql, nosql_client, compartments)
                    future_MYSQL = executor.submit(self.__load_database_mysql, mysql_client, compartments)
                    future_SOFTWARE_IMAGES = executor.submit(self.__load_database_software_images, database_client, compartments)
                    future_GG_DEPLOYMENTS = executor.submit(self.__load_database_gg_deployments, gg_client, compartments)
                    future_GG_DB_REGISTRATION = executor.submit(self.__load_database_gg_db_registration, gg_client, compartments)
                    future_EXTERNAL_CDB = executor.submit(self.__load_database_external_cdb, database_client, compartments)
                    future_EXTERNAL_PDB = executor.submit(self.__load_database_external_pdb, database_client, compartments)
                    future_EXTERNAL_NONPDB = executor.submit(self.__load_database_external_nonpdb, database_client, compartments)

                    # db homes fetch backups which depends on standalone backups
                    db[self.C_DATABASE_BACKUPS] += next(as_completed([future_BACKUPS])).result()
                    future_HOMES = executor.submit(self.__load_database_homes, database_client, compartments)

                    # VM Clusters and DB System depends on db homes
                    db[self.C_DATABASE_HOMES] += next(as_completed([future_HOMES])).result()
                    future_EXACC_VMS = executor.submit(self.__load_database_exacc_vm_clusters, database_client, virtual_network, compartments)
                    future_EXADATA_VMS = executor.submit(self.__load_database_exadata_vm_clusters, database_client, virtual_network, compartments)
                    future_DBSYSTEMS = executor.submit(self.__load_database_dbsystems, database_client, virtual_network, compartments)

                    db[self.C_DATABASE_EXACC] += next(as_completed([future_EXACC])).result()
                    db[self.C_DATABASE_EXACC_VMS] += next(as_completed([future_EXACC_VMS])).result()
                    db[self.C_DATABASE_EXACC_ADB_VMS] += next(as_completed([future_EXACC_ADB_VMS])).result()
                    db[self.C_DATABASE_EXADATA] += next(as_completed([future_EXADATA])).result()
                    db[self.C_DATABASE_EXADATA_VMS] += next(as_completed([future_EXADATA_VMS])).result()
                    db[self.C_DATABASE_DBSYSTEMS] += next(as_completed([future_DBSYSTEMS])).result()
                    db[self.C_DATABASE_ADB_D_VMS] += next(as_completed([future_ADB_D_VMS])).result()
                    db[self.C_DATABASE_ADB_D_CONTAINERS] += next(as_completed([future_ADB_D_CONTAINERS])).result()
                    db[self.C_DATABASE_ADB_DATABASE] += next(as_completed([future_ADB_DATABASE])).result()
                    db[self.C_DATABASE_NOSQL] += next(as_completed([future_NOSQL])).result()
                    db[self.C_DATABASE_MYSQL] += next(as_completed([future_MYSQL])).result()
                    db[self.C_DATABASE_SOFTWARE_IMAGES] += next(as_completed([future_SOFTWARE_IMAGES])).result()
                    db[self.C_DATABASE_GG_DEPLOYMENTS] += next(as_completed([future_GG_DEPLOYMENTS])).result()
                    db[self.C_DATABASE_GG_DB_REGISTRATION] += next(as_completed([future_GG_DB_REGISTRATION])).result()
                    db[self.C_DATABASE_EXTERNAL_CDB] += next(as_completed([future_EXTERNAL_CDB])).result()
                    db[self.C_DATABASE_EXTERNAL_PDB] += next(as_completed([future_EXTERNAL_PDB])).result()
                    db[self.C_DATABASE_EXTERNAL_NONPDB] += next(as_completed([future_EXTERNAL_NONPDB])).result()

            # Complete Database
            self.__load_print_section_time(section_start_time)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_section_database_main", e)

    ##########################################################################
    # __load_database_maintatance
    ##########################################################################
    def __load_database_maintatance(self, database_client, maintenance_run_id, db_system_name):
        try:
            if not maintenance_run_id:
                return {}

            # oci.database.models.MaintenanceRun
            mt = database_client.get_maintenance_run(maintenance_run_id).data
            val = {'id': str(mt.id),
                   'display_name': str(mt.display_name),
                   'description': str(mt.description),
                   'lifecycle_state': str(mt.lifecycle_state),
                   'time_scheduled': str(mt.time_scheduled),
                   'time_started': str(mt.time_started),
                   'time_ended': str(mt.time_ended),
                   'target_resource_type': str(mt.target_resource_type),
                   'target_resource_id': str(mt.target_resource_id),
                   'maintenance_type': str(mt.maintenance_type),
                   'maintenance_subtype': str(mt.maintenance_subtype),
                   'maintenance_display': str(mt.display_name) + " ( " + str(mt.maintenance_type) + ", " + str(mt.maintenance_subtype) + ", " + str(mt.lifecycle_state) + " ), Scheduled: " + str(mt.time_scheduled)[0:16] + ((", Execution: " + str(mt.time_started)[0:16] + " - " + str(mt.time_ended)[0:16]) if str(mt.time_started) != 'None' else ""),
                   'maintenance_alert': ""
                   }

            # If maintenane is less than 14 days
            if mt.time_scheduled:
                delta = mt.time_scheduled.date() - datetime.date.today()
                if delta.days <= 14 and delta.days >= 0 and not mt.time_started:
                    val['maintenance_alert'] = "DBSystem Maintenance is in " + str(delta.days).ljust(2, ' ') + " days, on " + str(mt.time_scheduled)[0:16] + " for " + db_system_name
                    self.dbsystem_maintenance.append(val['maintenance_alert'])
            return val

        except oci.exceptions.ServiceError:
            print("m", end="")
            return ""
        except oci.exceptions.RequestException:
            print("m", end="")
            return ""
        except Exception as e:
            self.__print_error("__load_database_maintatance", e)

    ##########################################################################
    # __load_database_maintatance_estimate_date
    ##########################################################################
    def __load_database_maintatance_estimate_date(self, input_months, input_week, input_day):
        try:
            # define output dates
            output_dates = []

            # pre defined months and days
            months_q1 = ['JANUARY', 'FEBRUARY', 'MARCH']
            months_q2 = ['APRIL', 'MAY', 'JUNE']
            months_q3 = ['JULY', 'AUGUST', 'SEPTEMBER']
            months_q4 = ['OCTOBER', 'NOVEMBER', 'DECEMBER']
            days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

            # limit to one month per quarter
            months_to_check = []
            for mm in months_q1:
                if mm in input_months:
                    months_to_check.append(mm)
                    break
            for mm in months_q2:
                if mm in input_months:
                    months_to_check.append(mm)
                    break
            for mm in months_q3:
                if mm in input_months:
                    months_to_check.append(mm)
                    break
            for mm in months_q4:
                if mm in input_months:
                    months_to_check.append(mm)
                    break

            # loop on future 365 days from tomorrow
            timeNow = datetime.datetime.now() + datetime.timedelta(days=1)
            for i in range(365):
                newDate = timeNow + datetime.timedelta(days=i)
                newWeek = (newDate.day - 1) // 7 + 1
                newMonth = newDate.strftime('%B').upper()
                newDay = days[newDate.weekday()]
                if newMonth in months_to_check and newWeek == input_week and newDay == input_day:
                    newDateStr = newDate.strftime('%d-%b-%Y')
                    output_dates.append(newDateStr)

            # result
            return output_dates

        except Exception as e:
            self.__print_error("__load_database_maintatance_estimate_date", e)

    ##########################################################################
    # __load_database_maintatance_windows
    ##########################################################################
    def __load_database_maintatance_windows(self, maintenance_window):
        try:
            if not maintenance_window:
                return {}

            mw = maintenance_window

            # estimate dates
            estimate_dates_str = ""
            if str(mw.preference) != "NO_PREFERENCE" and mw.months and mw.weeks_of_month and mw.days_of_week:
                array_months = [x.name for x in mw.months]
                week_of_month = [x for x in mw.weeks_of_month][0]
                day_of_week = [x.name for x in mw.days_of_week][0]
                estimate_dates = self.__load_database_maintatance_estimate_date(array_months, week_of_month, day_of_week)
                if estimate_dates:
                    estimate_dates_str = ", ".join([x for x in estimate_dates])

            value = {
                'preference': str(mw.preference),
                'months': ", ".join([x.name for x in mw.months]) if mw.months else "",
                'weeks_of_month': ", ".join([str(x) for x in mw.weeks_of_month]) if mw.weeks_of_month else "",
                'hours_of_day': ", ".join([str(x) for x in mw.hours_of_day]) if mw.hours_of_day else "",
                'days_of_week': ", ".join([str(x.name) for x in mw.days_of_week]) if mw.days_of_week else "",
                'lead_time_in_weeks': str(mw.lead_time_in_weeks) if mw.lead_time_in_weeks else "",
                'estimate_dates': estimate_dates_str
            }
            value['display'] = str(mw.preference) if str(mw.preference) == "NO_PREFERENCE" else (str(mw.preference) + ": Months: " + value['months'] + ", Weeks: " + value['weeks_of_month'] + ", DOW: " + value['days_of_week'] + ", Hours: " + value['hours_of_day'] + ", Lead Weeks: " + value['lead_time_in_weeks'] + ", Estimate Dates: " + estimate_dates_str)
            return value

        except Exception as e:
            self.__print_error("__load_database_maintatance_windows", e)

    ##########################################################################
    # __load_database_exacc_infrastructure
    ##########################################################################

    def __load_database_exacc_infrastructure(self, database_client, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "ExaCC Infrastructure"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # list db system
                list_exa = []
                try:
                    list_exa = oci.pagination.list_call_get_all_results(
                        database_client.list_exadata_infrastructures,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning("a", to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # loop on the Exadata infrastructure
                # dbs = oci.database.models.ExadataInfrastructureSummary
                for dbs in list_exa:
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    value = {'id': self.get_value(dbs.id),
                             'display_name': self.get_value(dbs.display_name),
                             'shape': self.get_value(dbs.shape),
                             'time_zone': self.get_value(dbs.time_zone),
                             'cpus_enabled': self.get_value(dbs.cpus_enabled),
                             'max_cpu_count': self.get_value(dbs.max_cpu_count),
                             'memory_size_in_gbs': self.get_value(dbs.memory_size_in_gbs),
                             'max_memory_in_gbs': self.get_value(dbs.max_memory_in_gbs),
                             'db_node_storage_size_in_gbs': self.get_value(dbs.db_node_storage_size_in_gbs),
                             'max_db_node_storage_in_g_bs': self.get_value(dbs.max_db_node_storage_in_g_bs),
                             'data_storage_size_in_tbs': self.get_value(str(dbs.data_storage_size_in_tbs)),
                             'max_data_storage_in_t_bs': self.get_value(dbs.max_data_storage_in_t_bs),
                             'storage_count': self.get_value(dbs.storage_count),
                             'compute_count': self.get_value(dbs.compute_count),
                             'additional_storage_count': self.get_value(dbs.additional_storage_count),
                             'activated_storage_count': self.get_value(dbs.activated_storage_count),
                             'cloud_control_plane_server1': self.get_value(dbs.cloud_control_plane_server1),
                             'cloud_control_plane_server2': self.get_value(dbs.cloud_control_plane_server2),
                             'netmask': self.get_value(dbs.netmask),
                             'gateway': self.get_value(dbs.gateway),
                             'admin_network_cidr': self.get_value(dbs.admin_network_cidr),
                             'infini_band_network_cidr': self.get_value(dbs.infini_band_network_cidr),
                             'corporate_proxy': self.get_value(dbs.corporate_proxy),
                             'dns_server': self.get_value(dbs.dns_server),
                             'ntp_server': self.get_value(dbs.ntp_server),
                             'time_created': self.get_value(dbs.time_created),
                             'lifecycle_state': self.get_value(dbs.lifecycle_state),
                             'lifecycle_details': self.get_value(dbs.lifecycle_details),
                             'csi_number': self.get_value(dbs.csi_number),
                             'maintenance_slo_status': self.get_value(dbs.maintenance_slo_status),
                             'maintenance_window': self.__load_database_maintatance_windows(dbs.maintenance_window),
                             'last_maintenance_run': self.__load_database_maintatance(database_client, dbs.last_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                             'next_maintenance_run': self.__load_database_maintatance(database_client, dbs.next_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'contacts': "" if dbs.contacts is None else str(', '.join(x.name for x in dbs.contacts)),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'region_name': str(self.config['region']),
                             'vm_clusters': [],
                             'db_servers': self.__load_database_exacc_dbservers(database_client, compartment, dbs.id)
                             }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_exadata_cc_infrastructure", e)
            return data

    ##########################################################################
    # __load_database_exacc_vm_clusters
    ##########################################################################
    def __load_database_exacc_vm_clusters(self, database_client, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "ExaCC VMClusters"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                vms = []
                try:
                    vms = database_client.list_vm_clusters(
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # arr = oci.database.models.VmClusterSummary
                for arr in vms:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    value = {
                        'id': str(arr.id),
                        'last_patch_history_entry_id': str(arr.last_patch_history_entry_id),
                        'lifecycle_state': str(arr.lifecycle_state),
                        'display_name': str(arr.display_name),
                        'time_created': str(arr.time_created),
                        'lifecycle_details': str(arr.lifecycle_details),
                        'time_zone': str(arr.time_zone),
                        'is_local_backup_enabled': str(arr.is_local_backup_enabled),
                        'exadata_infrastructure_id': str(arr.exadata_infrastructure_id),
                        'is_sparse_diskgroup_enabled': str(arr.is_sparse_diskgroup_enabled),
                        'vm_cluster_network_id': str(arr.vm_cluster_network_id),
                        'cpus_enabled': str(arr.cpus_enabled),
                        'memory_size_in_gbs': str(arr.memory_size_in_gbs),
                        'db_node_storage_size_in_gbs': str(arr.db_node_storage_size_in_gbs),
                        'data_storage_size_in_tbs': str(arr.data_storage_size_in_tbs),
                        'shape': str(arr.shape),
                        'gi_version': str(arr.gi_version),
                        'gi_version_date': self.get_database_gi_version_date(str(arr.gi_version)),
                        'system_version': str(arr.system_version),
                        'system_version_date': self.get_database_system_version_date(str(arr.system_version)),
                        'license_model': str(arr.license_model),
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'db_homes': self.__load_database_dbsystems_dbhomes(arr.id, exa=True),
                        'db_nodes': self.__load_database_dbsystems_dbnodes(database_client, virtual_network, compartment, arr.id, exa=True),
                        'patches': [],
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])
                    }

                    # license model
                    if arr.license_model == "LICENSE_INCLUDED":
                        value['license_model'] = "INCL"
                    elif arr.license_model == "BRING_YOUR_OWN_LICENSE":
                        value['license_model'] = "BYOL"
                    else:
                        value['license_model'] = str(arr.license_model)

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)

            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise

        except Exception as e:
            self.__print_error("__load_database_exacc_vm_clusters", e, compartment)
            return data

    ##########################################################################
    # __load_database_exacc_adb_vmclusters
    ##########################################################################
    def __load_database_exacc_adb_vmclusters(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "ExaCC VMClusters ADB"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # list_cloud_autonomous_vm_clusters
                list_vms = []
                try:
                    list_vms = oci.pagination.list_call_get_all_results(
                        database_client.list_autonomous_vm_clusters,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # dbs = oci.database.models.AutonomousVmClusterSummary
                for dbs in list_vms:
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    value = {'id': str(dbs.id),
                             'display_name': str(dbs.display_name),
                             'description': str(dbs.description),
                             'last_update_history_entry_id': str(dbs.last_update_history_entry_id),
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'lifecycle_details': str(dbs.lifecycle_details),
                             'time_created': str(dbs.time_created),
                             'time_zone': str(dbs.cluster_time_zone),
                             'shape': str(dbs.shape),
                             'exadata_infrastructure_id': str(dbs.exadata_infrastructure_id),
                             'vm_cluster_network_id': str(dbs.vm_cluster_network_id),
                             'is_local_backup_enabled': str(dbs.is_local_backup_enabled),
                             'cpus_enabled': str(dbs.cpus_enabled),
                             'ocpus_enabled': str(dbs.ocpus_enabled),
                             'available_cpus': str(dbs.available_cpus),
                             'total_container_databases': str(dbs.total_container_databases),
                             'memory_per_oracle_compute_unit_in_gbs': str(dbs.memory_per_oracle_compute_unit_in_gbs),
                             'cpu_core_count_per_node': str(dbs.cpu_core_count_per_node),
                             'autonomous_data_storage_size_in_tbs': str(dbs.autonomous_data_storage_size_in_tbs),
                             'memory_size_in_gbs': str(dbs.memory_size_in_gbs),
                             'db_node_storage_size_in_gbs': str(dbs.db_node_storage_size_in_gbs),
                             'data_storage_size_in_tbs': str(dbs.data_storage_size_in_tbs),
                             'data_storage_size_in_gbs': str(dbs.data_storage_size_in_gbs),
                             'available_data_storage_size_in_tbs': str(dbs.available_data_storage_size_in_tbs),
                             'reclaimable_cpus': str(dbs.license_reclaimable_cpusmodel),
                             'available_container_databases': str(dbs.available_container_databases),
                             'available_autonomous_data_storage_size_in_tbs': str(dbs.available_autonomous_data_storage_size_in_tbs),
                             'scan_listener_port_tls': str(dbs.scan_listener_port_tls),
                             'scan_listener_port_non_tls': str(dbs.scan_listener_port_non_tls),
                             'is_mtls_enabled': str(dbs.is_mtls_enabled),
                             'maintenance_window': self.__load_database_maintatance_windows(dbs.maintenance_window),
                             'last_maintenance_run': self.__load_database_maintatance(database_client, dbs.last_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                             'next_maintenance_run': self.__load_database_maintatance(database_client, dbs.next_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'region_name': str(self.config['region'])
                             }

                    # license model
                    if dbs.license_model == oci.database.models.AutonomousVmClusterSummary.LICENSE_MODEL_LICENSE_INCLUDED:
                        value['license_model'] = "INCL"
                    elif dbs.license_model == oci.database.models.AutonomousVmClusterSummary.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE:
                        value['license_model'] = "BYOL"
                    else:
                        value['license_model'] = str(dbs.license_model)

                    # get shape
                    if dbs.shape:
                        shape_sizes = self.get_shape_details(str(dbs.shape))
                        if shape_sizes:
                            value['shape_ocpu'] = shape_sizes['cpu']
                            value['shape_memory_gb'] = shape_sizes['memory']
                            value['shape_storage_tb'] = shape_sizes['storage']

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_exacc_adb_vmclusters", e, compartment)
            return data

    ##########################################################################
    # __load_database_exacc_dbservers
    ##########################################################################
    def __load_database_exacc_dbservers(self, database_client, compartment, dbs_id):

        db = self.data[self.C_DATABASE]
        data = []
        try:
            db_servers = database_client.list_db_servers(
                compartment['id'],
                exadata_infrastructure_id=dbs_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # db_server = oci.database.models.DbServerSummary
            for db_server in db_servers:

                value = {
                    'id': str(db_server.id),
                    'db_system_id': dbs_id,
                    'display_name': str(db_server.display_name),
                    'cpu_core_count': str(db_server.cpu_core_count),
                    'memory_size_in_gbs': str(db_server.memory_size_in_gbs),
                    'db_node_storage_size_in_gbs': str(db_server.db_node_storage_size_in_gbs),
                    'vm_cluster_ids': db_server.vm_cluster_ids,
                    'db_node_ids': db_server.db_node_ids,
                    'lifecycle_state': str(db_server.lifecycle_state),
                    'max_cpu_count': str(db_server.max_cpu_count),
                    'max_memory_in_gbs': str(db_server.max_memory_in_gbs),
                    'max_db_node_storage_in_gbs': str(db_server.max_db_node_storage_in_gbs),
                    'time_created': str(db_server.time_created),
                    'defined_tags': [] if db_server.defined_tags is None else db_server.defined_tags,
                    'freeform_tags': [] if db_server.freeform_tags is None else db_server.freeform_tags
                }

                cpu_info = ""
                if db_server.cpu_core_count:
                    cpu_info = " - Cores: " + str(db_server.cpu_core_count) + " / " + str(db_server.max_cpu_count)
                    cpu_info += " - Mem: " + str(db_server.memory_size_in_gbs) + " / " + str(db_server.max_memory_in_gbs)
                    cpu_info += " - Disk: " + str(db_server.db_node_storage_size_in_gbs) + " / " + str(db_server.max_db_node_storage_in_gbs)

                value['desc'] = str(db_server.display_name) + " - " + str(db_server.lifecycle_state) + cpu_info
                data.append(value)

            # add to main data
            db[self.C_DATABASE_EXACC_DBSERVERS] += data
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                print("Error at __load_database_exacc_dbservers")
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            else:
                print("Error at __load_database_exacc_dbservers")
                raise
        except Exception as e:
            self.__print_error("__load_database_exacc_dbservers", e)
            return data

    ##########################################################################
    # __load_database_exadata_infrastructure
    ##########################################################################

    def __load_database_exadata_infrastructure(self, database_client, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Exadata Infrastructure"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # list db system
                list_exa = []
                try:
                    list_exa = oci.pagination.list_call_get_all_results(
                        database_client.list_cloud_exadata_infrastructures,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # loop on the Exadata infrastructure
                # dbs = oci.database.models.CloudExadataInfrastructureSummary
                for dbs in list_exa:
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    value = {'id': str(dbs.id),
                             'display_name': str(dbs.display_name),
                             'shape': str(dbs.shape),
                             'shape_ocpu': 0,
                             'shape_memory_gb': 0,
                             'shape_storage_tb': 0,
                             'version': 'XP',
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'lifecycle_details': str(dbs.lifecycle_details),
                             'availability_domain': str(dbs.availability_domain),
                             'storage_count': str(dbs.storage_count) if dbs.storage_count else "",
                             'compute_count': str(dbs.compute_count) if dbs.compute_count else "",
                             'total_storage_size_in_gbs': str(dbs.total_storage_size_in_gbs),
                             'available_storage_size_in_gbs': str(dbs.available_storage_size_in_gbs),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'time_created': str(dbs.time_created),
                             'last_maintenance_run': self.__load_database_maintatance(database_client, dbs.last_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                             'next_maintenance_run': self.__load_database_maintatance(database_client, dbs.next_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                             'maintenance_window': self.__load_database_maintatance_windows(dbs.maintenance_window),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'region_name': str(self.config['region']),
                             'vm_clusters': [],
                             'db_servers': self.__load_database_exacc_dbservers(database_client, compartment, dbs.id)
                             }

                    # get shape
                    if dbs.shape:
                        shape_sizes = self.get_shape_details(str(dbs.shape))
                        if shape_sizes:
                            value['shape_ocpu'] = shape_sizes['cpu']
                            value['shape_memory_gb'] = shape_sizes['memory']
                            value['shape_storage_tb'] = shape_sizes['storage']

                        # if x8m calculate ocpu and storage
                        if dbs.shape == "Exadata.X8M":
                            if dbs.compute_count != "2" or dbs.storage_count != "3":
                                value['shape_ocpu'] = dbs.compute_count * 50
                                value['shape_storage_tb'] = dbs.storage_count * 49.5
                                value['shape_memory_gb'] = dbs.compute_count * 720

                        if dbs.shape == "Exadata.X9M":
                            if dbs.compute_count != "2" or dbs.storage_count != "3":
                                value['shape_ocpu'] = dbs.compute_count * 126
                                value['shape_storage_tb'] = dbs.storage_count * 64
                                value['shape_memory_gb'] = dbs.compute_count * 1300

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_exadata_infrastructure", e, compartment)
            return data

    ##########################################################################
    # __load_database_exadata_vm_clusters
    ##########################################################################
    def __load_database_exadata_vm_clusters(self, database_client, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Exadata VMClusters"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                vms = []
                try:
                    vms = database_client.list_cloud_vm_clusters(
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # arr = oci.database.models.CloudVmClusterSummary
                for arr in vms:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    value = {
                        'id': str(arr.id),
                        'cloud_exadata_infrastructure_id': str(arr.cloud_exadata_infrastructure_id),
                        'cluster_name': str(arr.cluster_name),
                        'hostname': str(arr.hostname),
                        'availability_domain': str(arr.availability_domain),
                        'data_subnet_id': str(arr.subnet_id),
                        'data_subnet': self.get_network_subnet(str(arr.subnet_id), True),
                        'backup_subnet_id': str(arr.backup_subnet_id),
                        'backup_subnet': "" if arr.backup_subnet_id is None else self.get_network_subnet(str(arr.backup_subnet_id), True),
                        'nsg_ids': arr.nsg_ids,
                        'backup_network_nsg_ids': str(arr.backup_network_nsg_ids),
                        'last_update_history_entry_id': str(arr.last_update_history_entry_id),
                        'shape': str(arr.shape),
                        'listener_port': str(arr.listener_port),
                        'lifecycle_state': str(arr.lifecycle_state),
                        'node_count': str(arr.node_count),
                        'storage_size_in_gbs': str(arr.storage_size_in_gbs),
                        'display_name': str(arr.display_name),
                        'time_created': str(arr.time_created),
                        'lifecycle_details': str(arr.lifecycle_details),
                        'time_zone': str(arr.time_zone),
                        'domain': str(arr.domain),
                        'cpu_core_count': str(arr.cpu_core_count),
                        'data_storage_percentage': str(arr.data_storage_percentage),
                        'is_local_backup_enabled': str(arr.is_local_backup_enabled),
                        'is_sparse_diskgroup_enabled': str(arr.is_sparse_diskgroup_enabled),
                        'gi_version': str(arr.gi_version),
                        'gi_version_date': self.get_database_gi_version_date(str(arr.gi_version)),
                        'system_version': str(arr.system_version),
                        'system_version_date': self.get_database_system_version_date(str(arr.system_version)),
                        'ssh_public_keys': str(arr.ssh_public_keys),
                        'license_model': str(arr.license_model),
                        'disk_redundancy': str(arr.disk_redundancy),
                        'scan_ip_ids': str(arr.scan_ip_ids),
                        'vip_ids': str(arr.vip_ids),
                        'scan_dns_record_id': str(arr.scan_dns_record_id),
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'patches': [],
                        'db_homes': self.__load_database_dbsystems_dbhomes(arr.id, exa=True),
                        'db_nodes': self.__load_database_dbsystems_dbnodes(database_client, virtual_network, compartment, arr.id, exa=True),
                        'region_name': str(self.config['region']),
                        'scan_ips': [],
                        'vip_ips': [],
                        'scan_dns_name': str(arr.scan_dns_name),
                        'zone_id': str(arr.zone_id),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id'])
                    }

                    # Skip the patches, there is an issue with the api for the vm cluster
                    # value['patches'] = self.__load_database_exadata_vm_patches(database_client, arr.id),

                    # get shape
                    if arr.shape:
                        shape_sizes = self.get_shape_details(str(arr.shape))
                        if shape_sizes:
                            value['shape_ocpu'] = shape_sizes['cpu']
                            value['shape_memory_gb'] = shape_sizes['memory']
                            value['shape_storage_tb'] = shape_sizes['storage']

                    # license model
                    if arr.license_model == oci.database.models.CloudVmClusterSummary.LICENSE_MODEL_LICENSE_INCLUDED:
                        value['license_model'] = "INCL"
                    elif arr.license_model == oci.database.models.CloudVmClusterSummary.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE:
                        value['license_model'] = "BYOL"
                    else:
                        value['license_model'] = str(arr.license_model)

                    # scan IPs
                    if arr.scan_ip_ids is not None:
                        scan_ips = []
                        for scan_ip in arr.scan_ip_ids:
                            scan_ips.append(self.__load_core_network_single_privateip(virtual_network, scan_ip))
                        value['scan_ips'] = scan_ips

                    # VIPs
                    if arr.vip_ids is not None:
                        vip_ips = []
                        for vipip in arr.vip_ids:
                            vip_ips.append(self.__load_core_network_single_privateip(virtual_network, vipip))
                        value['vip_ips'] = vip_ips

                    # add to main data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_exadata_vm_clusters", e, compartment)
            return data

    ##########################################################################
    # __load_database_homes
    ##########################################################################
    def __load_database_homes(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Database Homes"
            self.__load_print_status_with_threads(header)

            # if skip db homes
            if self.flags.skip_dbhomes:
                self.__load_print_thread_cnt(header, cnt, start_time, "Skipped.")
                return data

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                homes = []
                try:
                    homes = database_client.list_db_homes(
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # arr = oci.database.models.DbHomeSummary
                for db_home in homes:
                    if not self.check_lifecycle_state_active(db_home.lifecycle_state):
                        continue

                    value = {
                        'id': str(db_home.id),
                        'display_name': str(db_home.display_name),
                        'last_patch_history_entry_id': str(db_home.last_patch_history_entry_id),
                        'lifecycle_state': str(db_home.lifecycle_state),
                        'db_system_id': str(db_home.db_system_id),
                        'vm_cluster_id': str(db_home.vm_cluster_id),
                        'db_version': str(db_home.db_version),
                        'db_home_location': str(db_home.db_home_location),
                        'kms_key_id': str(db_home.kms_key_id),
                        'one_off_patches': db_home.one_off_patches,
                        'database_software_image_id': db_home.database_software_image_id,
                        'time_created': str(db_home.time_created),
                        'compartment_id': str(db_home.compartment_id),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'defined_tags': [] if db_home.defined_tags is None else db_home.defined_tags,
                        'freeform_tags': [] if db_home.freeform_tags is None else db_home.freeform_tags,
                        'databases': self.__load_database_dbsystems_dbhomes_databases(database_client, db_home.id, compartment),
                        'patches': self.__load_database_dbsystems_home_patches(database_client, db_home.id),
                        'patches_history': self.__load_database_dbsystems_home_patches_history(database_client, db_home.id)
                    }

                    # add to main data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_db_homes", e, compartment)
            return data

    ##########################################################################
    # __load_database_backups
    ##########################################################################
    def __load_database_standalone_backups(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Database Standalone Backups"

            if self.flags.skip_backups:
                self.__load_print_thread_cnt(header, cnt, start_time, "Skipped.")
                return data

            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                backups = []
                try:
                    backups = oci.pagination.list_call_get_all_results(
                        database_client.list_backups,
                        compartment_id=compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                for backup in backups:
                    if not self.check_lifecycle_state_active(backup.lifecycle_state):
                        continue

                    value = {
                        'id': str(backup.id),
                        'display_name': str(backup.display_name),
                        'database_id': str(backup.database_id),
                        'standalone': True,
                        'type': str(backup.type),
                        'time_started': str(backup.time_started),
                        'time_ended': str(backup.time_ended),
                        'lifecycle_state': str(backup.lifecycle_state),
                        'lifecycle_details': str(backup.lifecycle_details),
                        'availability_domain': str(backup.availability_domain),
                        'database_edition': self.get_database_short_edition(backup.database_edition),
                        'shape': str(backup.shape),
                        'version': str(backup.version),
                        'kms_key_id': str(backup.kms_key_id) if backup.kms_key_id else "",
                        'kms_key_version_id': str(backup.kms_key_version_id) if backup.kms_key_version_id else "",
                        'vault_id': str(backup.vault_id) if backup.vault_id else "",
                        'database_size_in_gbs': "" if backup.database_size_in_gbs is None else str(backup.database_size_in_gbs),
                        'compartment_id': str(compartment['id']),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'region_name': str(self.config['region'])}

                    # add to main data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_standalone_backups", e, compartment)
            return data

    ##########################################################################
    # __load_database_exadata_vm_patches
    ##########################################################################
    def __load_database_exadata_vm_patches(self, database_client, vm_id):

        data = []
        try:
            dbps = oci.pagination.list_call_get_all_results(
                database_client.list_vm_cluster_patches,
                vm_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            for dbp in dbps:
                data.append({'id': dbp.id, 'description': str(dbp.description),
                             'version': str(dbp.version), 'time_released': str(dbp.time_released),
                             'last_action': str(dbp.last_action)})
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_exadata_vm_patches", e)
            return data

    ##########################################################################
    # __load_database_dbsystems
    ##########################################################################

    def __load_database_dbsystems(self, database_client, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "DB Systems"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # list db system
                list_db_systems = []
                try:
                    list_db_systems = oci.pagination.list_call_get_all_results(
                        database_client.list_db_systems,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # loop on the db systems
                # dbs = oci.database.models.DbSystemSummary
                for dbs in list_db_systems:
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    value = {'id': str(dbs.id),
                             'display_name': str(dbs.display_name),
                             'shape': str(dbs.shape),
                             'shape_ocpu': 0,
                             'shape_memory_gb': 0,
                             'shape_storage_tb': 0,
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'data_storage_size_in_gbs': "" if dbs.data_storage_size_in_gbs is None else str(dbs.data_storage_size_in_gbs),
                             'availability_domain': str(dbs.availability_domain),
                             'cpu_core_count': str(dbs.cpu_core_count),
                             'node_count': ("" if dbs.node_count is None else str(dbs.node_count)),
                             'version': str(dbs.version),
                             'version_date': self.get_database_gi_version_date(str(dbs.version)),
                             'hostname': str(dbs.hostname),
                             'domain': str(dbs.domain),
                             'data_storage_percentage': str(dbs.data_storage_percentage),
                             'data_subnet': self.get_network_subnet(str(dbs.subnet_id), True),
                             'data_subnet_id': str(dbs.subnet_id),
                             'backup_subnet': "" if dbs.backup_subnet_id is None else self.get_network_subnet(str(dbs.backup_subnet_id), True),
                             'backup_subnet_id': str(dbs.backup_subnet_id),
                             'scan_dns_record_id': "" if dbs.scan_dns_record_id is None else str(dbs.scan_dns_record_id),
                             'listener_port': str(dbs.listener_port),
                             'cluster_name': "" if dbs.cluster_name is None else str(dbs.cluster_name),
                             'database_edition': str(dbs.database_edition),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'time_created': str(dbs.time_created),
                             'storage_management': "",
                             'sparse_diskgroup': str(dbs.sparse_diskgroup),
                             'reco_storage_size_in_gb': str(dbs.reco_storage_size_in_gb),
                             'last_maintenance_run': self.__load_database_maintatance(database_client, dbs.last_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                             'next_maintenance_run': self.__load_database_maintatance(database_client, dbs.next_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                             'maintenance_window': self.__load_database_maintatance_windows(dbs.maintenance_window),
                             'region_name': str(self.config['region']),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'patches': self.__load_database_dbsystems_patches(database_client, dbs.id),
                             'db_nodes': self.__load_database_dbsystems_dbnodes(database_client, virtual_network, compartment, dbs.id),
                             'db_homes': self.__load_database_dbsystems_dbhomes(dbs.id),
                             'scan_dns_name': "" if dbs.scan_dns_name is None else str(dbs.scan_dns_name),
                             'zone_id': str(dbs.zone_id),
                             }

                    value['database_edition_short'] = self.get_database_short_edition(dbs.database_edition)
                    value['license_model'] = self.get_database_short_license(dbs.license_model)

                    # get shape
                    if dbs.shape:
                        shape_sizes = self.get_shape_details(str(dbs.shape))
                        if shape_sizes:
                            value['shape_ocpu'] = shape_sizes['cpu']
                            value['shape_memory_gb'] = shape_sizes['memory']
                            value['shape_storage_tb'] = shape_sizes['storage']

                    # storage_management
                    if dbs.db_system_options:
                        if dbs.db_system_options.storage_management:
                            value['storage_management'] = dbs.db_system_options.storage_management

                    # scan IPs
                    value['scan_ips'] = []
                    if dbs.scan_ip_ids is not None:
                        scan_ips = []
                        for scan_ip in dbs.scan_ip_ids:
                            scan_ips.append(self.__load_core_network_single_privateip(virtual_network, scan_ip))
                        value['scan_ips'] = scan_ips

                    # VIPs
                    value['vip_ips'] = []
                    if dbs.vip_ids is not None:
                        vip_ips = []
                        for vipip in dbs.vip_ids:
                            vip_ips.append(self.__load_core_network_single_privateip(virtual_network, vipip))
                        value['vip_ips'] = vip_ips

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems", e, compartment)
            return data

    ##########################################################################
    # __load_database_exadata_infrastructure
    ##########################################################################
    def __load_database_dbsystems_dbnodes(self, database_client, virtual_network, compartment, dbs_id, exa=False):

        data = []
        db_nodes = []
        api_call = ""
        try:
            if not exa:
                api_call = "database_client.list_db_nodes with db_system_id"
                db_nodes = database_client.list_db_nodes(
                    compartment['id'],
                    db_system_id=dbs_id,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data
            else:
                api_call = "database_client.list_db_nodes with vm_cluster_id"
                db_nodes = database_client.list_db_nodes(
                    compartment['id'],
                    vm_cluster_id=dbs_id,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

            # db_node = oci.database.models.DbNodeSummary
            for db_node in db_nodes:
                data.append(
                    {'id': str(db_node.id),
                     'hostname': str(db_node.hostname),
                     'fault_domain': str(db_node.fault_domain),
                     'lifecycle_state': str(db_node.lifecycle_state),
                     'vnic_id': str(db_node.vnic_id),
                     'backup_vnic_id': str(db_node.backup_vnic_id),
                     'cpu_core_count': str(db_node.cpu_core_count),
                     'memory_size_in_gbs': str(db_node.memory_size_in_gbs),
                     'db_node_storage_size_in_gbs': str(db_node.db_node_storage_size_in_gbs),
                     'db_server_id': str(db_node.db_server_id),
                     'maintenance_type': str(db_node.maintenance_type),
                     'time_maintenance_window_start': str(db_node.time_maintenance_window_start),
                     'time_maintenance_window_end': str(db_node.time_maintenance_window_end),
                     'vnic_details': self.__load_core_compute_vnic(virtual_network, str(db_node.vnic_id)),
                     'backup_vnic_details': self.__load_core_compute_vnic(virtual_network, str(db_node.backup_vnic_id)),
                     'software_storage_size_in_gb': str(db_node.software_storage_size_in_gb)})

                # mark reboot migration flag
                if db_node.maintenance_type is not None:
                    self.reboot_migration_counter += 1

            # add to main data
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                print("Error at API " + api_call)
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            else:
                print("Error at API " + api_call)
                raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_dbnodes, API=" + api_call, e)
            return data

    ##########################################################################
    # __load_database_dbsystems_dbhomes
    ##########################################################################
    def __load_database_dbsystems_dbhomes(self, dbs_id, exa=False):

        if not exa:
            return self.search_multi_items(self.C_DATABASE, self.C_DATABASE_HOMES, 'db_system_id', dbs_id)
        else:
            return self.search_multi_items(self.C_DATABASE, self.C_DATABASE_HOMES, 'vm_cluster_id', dbs_id)

    ##########################################################################
    # __load_database_dbsystems_db_backups
    ##########################################################################
    def __load_database_dbsystems_db_backups(self, database_client, db_id, compartment):

        data = []
        try:
            backups = oci.pagination.list_call_get_all_results(
                database_client.list_backups,
                database_id=db_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            for backup in backups:
                value = {
                    'id': str(backup.id),
                    'display_name': str(backup.display_name),
                    'database_id': str(backup.database_id),
                    'standalone': False,
                    'type': str(backup.type),
                    'time_started': str(backup.time_started),
                    'time_ended': str(backup.time_ended),
                    'lifecycle_state': str(backup.lifecycle_state),
                    'lifecycle_details': str(backup.lifecycle_details),
                    'availability_domain': str(backup.availability_domain),
                    'database_edition': self.get_database_short_edition(backup.database_edition),
                    'shape': str(backup.shape),
                    'version': str(backup.version),
                    'kms_key_id': str(backup.kms_key_id) if backup.kms_key_id else "",
                    'kms_key_version_id': str(backup.kms_key_version_id) if backup.kms_key_version_id else "",
                    'vault_id': str(backup.vault_id) if backup.vault_id else "",
                    'database_size_in_gbs': "" if backup.database_size_in_gbs is None else str(backup.database_size_in_gbs),
                    'compartment_id': str(compartment['id']),
                    'compartment_name': str(compartment['name']),
                    'compartment_path': str(compartment['path']),
                    'region_name': str(self.config['region'])}

                data.append(value)

                # add to main backup array if not exist
                db = self.data[self.C_DATABASE]
                bk = db[self.C_DATABASE_BACKUPS]
                if not any(d['id'] == str(backup.id) for d in bk):
                    bk.append(value)

            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_patches", e)
            return data

    ##########################################################################
    # __load_database_dbsystems_dbhomes_databases
    ##########################################################################

    def __load_database_dbsystems_dbhomes_databases(self, database_client, db_home_id, compartment):

        data = []
        try:
            dbs = oci.pagination.list_call_get_all_results(
                database_client.list_databases,
                compartment['id'],
                db_home_id=db_home_id,
                sort_by="DBNAME",
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # db = oci.database.models.DatabaseSummary
            for db in dbs:
                if not self.check_lifecycle_state_active(db.lifecycle_state):
                    continue

                value = {
                    'id': str(db.id),
                    'compartment_id': str(db.compartment_id),
                    'character_set': str(db.character_set),
                    'ncharacter_set': str(db.ncharacter_set),
                    'db_home_id': str(db.db_home_id),
                    'db_name': str(db.db_name),
                    'pdb_name': "" if db.pdb_name is None else str(db.pdb_name),
                    'db_workload': str(db.db_workload),
                    'db_unique_name': str(db.db_unique_name),
                    'lifecycle_details': str(db.lifecycle_details),
                    'lifecycle_state': str(db.lifecycle_state),
                    'defined_tags': [] if db.defined_tags is None else db.defined_tags,
                    'freeform_tags': [] if db.freeform_tags is None else db.freeform_tags,
                    'time_created': str(db.time_created),
                    'last_backup_timestamp': str(db.last_backup_timestamp),
                    'kms_key_id': str(db.kms_key_id),
                    'vault_id': str(db.vault_id),
                    'source_database_point_in_time_recovery_timestamp': str(db.source_database_point_in_time_recovery_timestamp),
                    'database_software_image_id': str(db.database_software_image_id),
                    'is_cdb': str(db.is_cdb),
                    'sid_prefix': str(db.sid_prefix),
                    'connection_strings_cdb': "",
                    'auto_backup_enabled': False,
                    'dataguard': self.__load_database_dbsystems_db_dg(database_client, db.id),
                    'backups': [] if self.flags.skip_backups else self.__load_database_dbsystems_db_backups(database_client, db.id, compartment),
                    'pdbs': self.__load_database_dbsystems_dbhomes_databases_pdbs(database_client, db.id)
                }

                if db.db_backup_config is not None:
                    if db.db_backup_config.auto_backup_enabled:
                        value['auto_backup_enabled'] = True

                if db.connection_strings is not None:
                    if db.connection_strings.cdb_default:
                        value['connection_strings_cdb'] = db.connection_strings.cdb_default

                data.append(value)

            # add to main data
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning("d")
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_dbhomes_databases", e)
            return data

    ##########################################################################
    # __load_database_dbsystems_dbhomes_databases_pdbs
    ##########################################################################

    def __load_database_dbsystems_dbhomes_databases_pdbs(self, database_client, dbid):

        data = []
        try:
            dbs = oci.pagination.list_call_get_all_results(
                database_client.list_pluggable_databases,
                database_id=dbid,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # db = oci.database.models.PluggableDatabaseSummary
            for db in dbs:
                if not self.check_lifecycle_state_active(db.lifecycle_state):
                    continue

                value = {
                    'id': str(db.id),
                    'pdb_name': str(db.pdb_name),
                    'container_database_id': str(db.container_database_id),
                    'lifecycle_details': str(db.lifecycle_details),
                    'lifecycle_state': str(db.lifecycle_state),
                    'compartment_id': str(db.compartment_id),
                    'connection_strings': "",
                    'open_mode': str(db.open_mode),
                    'is_restricted': str(db.is_restricted),
                    'defined_tags': [] if db.defined_tags is None else db.defined_tags,
                    'freeform_tags': [] if db.freeform_tags is None else db.freeform_tags
                }

                if db.connection_strings is not None:
                    if db.connection_strings.pdb_default:
                        value['connection_strings'] = db.connection_strings.pdb_default

                data.append(value)

            return data

        # OCI pluggable database management is supported only for Oracle Database 19.0 or higher
        except Exception:
            return data

    ##########################################################################
    # get db system patches
    ##########################################################################
    def __load_database_dbsystems_home_patches(self, database_client, dbhome_id):

        data = []
        try:
            dbps = oci.pagination.list_call_get_all_results(
                database_client.list_db_home_patches,
                dbhome_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            for dbp in dbps:
                data.append({'id': dbp.id, 'description': str(dbp.description), 'version': str(dbp.version), 'time_released': str(dbp.time_released),
                             'last_action': str(dbp.last_action)})
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                return data
            else:
                # Added in order to avoid internal error which happen often here
                if 'InternalError' in str(e.code):
                    print('p', end="")
                    return data
                if 'Aborted' in str(e.code):
                    print('p', end="")
                    return data
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_home_patches", e)
            return data

    ##########################################################################
    # get db system patches history
    ##########################################################################
    def __load_database_dbsystems_home_patches_history(self, database_client, dbhome_id):

        data = []
        try:
            dbps = oci.pagination.list_call_get_all_results(
                database_client.list_db_home_patch_history_entries,
                dbhome_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            for dbp in dbps:
                patch_description = dbp.patch_id

                # get patch info
                try:
                    patch = database_client.get_db_home_patch(dbhome_id, dbp.patch_id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                    patch_description = patch.description + " - " + patch.version
                except Exception:
                    pass

                # Add data
                data.append({'id': dbp.id, 'description': str(patch_description), 'action': str(dbp.action), 'lifecycle_state': str(dbp.lifecycle_state),
                             'time_started': str(dbp.time_started), 'time_ended': str(dbp.time_ended)})
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                return data
            else:
                # Added in order to avoid internal error which happen often here
                if 'InternalError' in str(e.code):
                    print('p', end="")
                    return data
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_home_patches_history", e)
            return data

    ##########################################################################
    # get db system patches
    ##########################################################################
    def __load_database_dbsystems_patches(self, database_client, dbs_id):

        data = []
        try:
            dbps = oci.pagination.list_call_get_all_results(
                database_client.list_db_system_patches,
                dbs_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            for dbp in dbps:
                data.append({'id': dbp.id, 'description': str(dbp.description),
                             'version': str(dbp.version), 'time_released': str(dbp.time_released),
                             'last_action': str(dbp.last_action)})
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_patches", e)
            return data

    ##########################################################################
    # get db system patches
    ##########################################################################
    def __load_database_dbsystems_db_dg(self, database_client, db_id):

        data = []
        try:
            dgs = oci.pagination.list_call_get_all_results(
                database_client.list_data_guard_associations,
                database_id=db_id,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # dg = oci.database.models.DataGuardAssociationSummary
            for dg in dgs:
                if not dg.peer_database_id or not self.check_lifecycle_state_active(dg.lifecycle_state):
                    continue

                val = ({'id': str(dg.id),
                        'database_id': str(dg.database_id),
                        'db_name': "",
                        'role': str(dg.role),
                        'peer_role': str(dg.peer_role),
                        'lifecycle_state': str(dg.lifecycle_state),
                        'peer_database_id': str(dg.peer_database_id),
                        'peer_data_guard_association_id': str(dg.peer_data_guard_association_id),
                        'apply_rate': str(dg.apply_rate),
                        'apply_lag': str(dg.apply_lag),
                        'protection_mode': str(dg.protection_mode),
                        'transport_type': str(dg.transport_type),
                        'time_created': str(dg.time_created)})

                # get db name
                try:
                    database = database_client.get_database(dg.peer_database_id).data
                    dbsystem = database_client.get_db_system(dg.peer_db_system_id).data
                    if database and dbsystem:
                        val['db_name'] = str(dbsystem.display_name) + ":" + str(database.db_unique_name)
                except Exception:
                    # incase error use ocid
                    val['db_name'] = str(dg.peer_db_system_id)

                # add the data
                data.append(val)

            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_dbsystems_db_dg", e)
            return data

    ##########################################################################
    # __load_database_adb_d_vmclusters
    ##########################################################################
    def __load_database_adb_d_vmclusters(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "ADB-D VMClusters"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # list_cloud_autonomous_vm_clusters
                list_vms = []
                try:
                    list_vms = oci.pagination.list_call_get_all_results(
                        database_client.list_cloud_autonomous_vm_clusters,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # loop on the Exadata infrastructure
                # dbs = oci.database.models.CloudAutonomousVmClusterSummary
                for dbs in list_vms:
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    value = {
                        'id': str(dbs.id),
                        'display_name': str(dbs.display_name),
                        'availability_domain': str(dbs.availability_domain),
                        'description': str(dbs.description),
                        'subnet_id': str(dbs.subnet_id),
                        'subnet_name': self.get_network_subnet(str(dbs.subnet_id), True),
                        'nsg_ids': dbs.nsg_ids,
                        'last_update_history_entry_id': str(dbs.last_update_history_entry_id),
                        'lifecycle_state': str(dbs.lifecycle_state),
                        'time_created': str(dbs.time_created),
                        'time_updated': str(dbs.time_updated),
                        'cluster_time_zone': str(dbs.cluster_time_zone),
                        'lifecycle_details': str(dbs.lifecycle_details),
                        'shape': str(dbs.shape),
                        'node_count': str(dbs.node_count),
                        'data_storage_size_in_tbs': str(dbs.data_storage_size_in_tbs),
                        'data_storage_size_in_gbs': str(dbs.data_storage_size_in_gbs),
                        'cpu_core_count': str(dbs.cpu_core_count),
                        'ocpu_count': str(dbs.ocpu_count),
                        'cpu_core_count_per_node': str(dbs.cpu_core_count_per_node),
                        'memory_size_in_gbs': str(dbs.memory_size_in_gbs),
                        'license_model': str(dbs.license_model),
                        'cloud_exadata_infrastructure_id': str(dbs.cloud_exadata_infrastructure_id),
                        'hostname': str(dbs.hostname),
                        'domain': str(dbs.domain),
                        'available_cpus': str(dbs.available_cpus),
                        'reclaimable_cpus': str(dbs.reclaimable_cpus),
                        'available_container_databases': str(dbs.available_container_databases),
                        'total_container_databases': str(dbs.total_container_databases),
                        'available_autonomous_data_storage_size_in_tbs': str(dbs.available_autonomous_data_storage_size_in_tbs),
                        'autonomous_data_storage_size_in_tbs': str(dbs.autonomous_data_storage_size_in_tbs),
                        'db_node_storage_size_in_gbs': str(dbs.db_node_storage_size_in_gbs),
                        'memory_per_oracle_compute_unit_in_gbs': str(dbs.memory_per_oracle_compute_unit_in_gbs),
                        'maintenance_window': self.__load_database_maintatance_windows(dbs.maintenance_window),
                        'last_maintenance_run': self.__load_database_maintatance(database_client, dbs.last_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                        'next_maintenance_run': self.__load_database_maintatance(database_client, dbs.next_maintenance_run_id, str(dbs.display_name) + " - " + str(dbs.shape)),
                        'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                        'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'compute_model': str(dbs.compute_model),
                        'is_mtls_enabled_vm_cluster': str(dbs.is_mtls_enabled_vm_cluster),
                        'scan_listener_port_tls': str(dbs.scan_listener_port_tls),
                        'scan_listener_port_non_tls': str(dbs.scan_listener_port_non_tls),
                        'time_database_ssl_certificate_expires': str(dbs.time_database_ssl_certificate_expires),
                        'time_ords_certificate_expires': str(dbs.time_ords_certificate_expires),
                        'region_name': str(self.config['region'])}

                    # license model
                    if dbs.license_model == oci.database.models.CloudAutonomousVmClusterSummary.LICENSE_MODEL_LICENSE_INCLUDED:
                        value['license_model'] = "INCL"
                    elif dbs.license_model == oci.database.models.CloudAutonomousVmClusterSummary.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE:
                        value['license_model'] = "BYOL"
                    else:
                        value['license_model'] = str(dbs.license_model)

                    # get shape
                    if dbs.shape:
                        shape_sizes = self.get_shape_details(str(dbs.shape))
                        if shape_sizes:
                            value['shape_ocpu'] = shape_sizes['cpu']
                            value['shape_memory_gb'] = shape_sizes['memory']
                            value['shape_storage_tb'] = shape_sizes['storage']

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_adb_d_vmclusters", e, compartment)
            return data

    ##########################################################################
    # __load_database_adb_d_containers
    ##########################################################################
    def __load_database_adb_d_containers(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "ADB-D Containers"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # list_autonomous_container_databases
                vms = []
                try:
                    vms = database_client.list_autonomous_container_databases(
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # arr = oci.database.models.AutonomousContainerDatabaseSummary
                for arr in vms:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    value = {
                        'id': str(arr.id),
                        'display_name': str(arr.display_name),
                        'db_unique_name': str(arr.db_unique_name),
                        'service_level_agreement_type': str(arr.service_level_agreement_type),
                        'autonomous_exadata_infrastructure_id': str(arr.autonomous_exadata_infrastructure_id),
                        'autonomous_vm_cluster_id': str(arr.autonomous_vm_cluster_id),
                        'cloud_autonomous_vm_cluster_id': str(arr.cloud_autonomous_vm_cluster_id),
                        'infrastructure_type': str(arr.infrastructure_type),
                        'kms_key_id': str(arr.kms_key_id),
                        'vault_id': str(arr.vault_id),
                        'lifecycle_state': str(arr.lifecycle_state),
                        'lifecycle_details': str(arr.lifecycle_details),
                        'time_created': str(arr.time_created),
                        'patch_model': str(arr.patch_model),
                        'patch_id': str(arr.patch_id),
                        'maintenance_window': self.__load_database_maintatance_windows(arr.maintenance_window),
                        'last_maintenance_run': self.__load_database_maintatance(database_client, arr.last_maintenance_run_id, str(arr.display_name)),
                        'next_maintenance_run': self.__load_database_maintatance(database_client, arr.next_maintenance_run_id, str(arr.display_name)),
                        'standby_maintenance_buffer_in_days': str(arr.standby_maintenance_buffer_in_days),
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'role': str(arr.role),
                        'availability_domain': str(arr.availability_domain),
                        'db_version': str(arr.db_version),
                        'key_store_id': str(arr.key_store_id),
                        'key_store_wallet_name': str(arr.key_store_wallet_name),
                        'compute_model': str(arr.compute_model),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])
                    }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_adb_d_containers", e, compartment)
            return data

    ##########################################################################
    # __load_database_autonomouns
    ##########################################################################
    def __load_database_adb_database(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "ADB-X Databases"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                list_autos = []
                try:
                    list_autos = oci.pagination.list_call_get_all_results(
                        database_client.list_autonomous_databases,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # loop on auto
                # dbs = oci.database.models.AutonomousDatabaseSummary
                for dbs in list_autos:
                    value = {}
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    value = {'id': str(dbs.id),
                             'display_name': str(dbs.display_name),
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'data_storage_size_in_tbs': str(dbs.data_storage_size_in_tbs),
                             'db_name': str(dbs.db_name),
                             'cpu_core_count': self.get_value(dbs.cpu_core_count),
                             'sum_count': ("0" if dbs.lifecycle_state == oci.database.models.AutonomousDatabaseSummary.LIFECYCLE_STATE_STOPPED else str(dbs.cpu_core_count)),
                             'db_version': self.get_value(dbs.db_version),
                             'service_console_url': self.get_value(dbs.service_console_url),
                             'connection_strings': "",
                             'connection_urls': self.get_value(dbs.connection_urls),
                             'time_created': self.get_value(dbs.time_created),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'region_name': str(self.config['region']),
                             'whitelisted_ips': "" if dbs.whitelisted_ips is None else str(', '.join(x for x in dbs.whitelisted_ips)),
                             'db_workload': str(dbs.db_workload),
                             'db_type': ("ATP" if str(dbs.db_workload) == "OLTP" else "ADWC"),
                             'is_auto_scaling_enabled': dbs.is_auto_scaling_enabled,
                             'is_dedicated': dbs.is_dedicated,
                             'subnet_id': self.get_value(dbs.subnet_id),
                             'data_safe_status': self.get_value(dbs.data_safe_status),
                             'time_maintenance_begin': self.get_value(dbs.time_maintenance_begin),
                             'time_maintenance_end': self.get_value(dbs.time_maintenance_end),
                             'nsg_ids': dbs.nsg_ids,
                             'private_endpoint': self.get_value(dbs.private_endpoint),
                             'private_endpoint_label': self.get_value(dbs.private_endpoint_label),
                             'backups': [],
                             'autonomous_container_database_id': self.get_value(dbs.autonomous_container_database_id),
                             'is_data_guard_enabled': dbs.is_data_guard_enabled,
                             'is_free_tier': dbs.is_free_tier,
                             'is_preview': dbs.is_preview,
                             'infrastructure_type': self.get_value(dbs.infrastructure_type),
                             'time_deletion_of_free_autonomous_database': self.get_value(dbs.time_deletion_of_free_autonomous_database),
                             'time_reclamation_of_free_autonomous_database': self.get_value(dbs.time_reclamation_of_free_autonomous_database),
                             'system_tags': dbs.system_tags,
                             'time_of_last_switchover': self.get_value(dbs.time_of_last_switchover),
                             'time_of_last_failover': self.get_value(dbs.time_of_last_failover),
                             'failed_data_recovery_in_seconds': self.get_value(dbs.failed_data_recovery_in_seconds),
                             'standby_lag_time_in_seconds': "",
                             'standby_lifecycle_state': "",
                             'peer_db_ids': dbs.peer_db_ids,
                             'time_data_guard_role_changed': self.get_value(dbs.time_data_guard_role_changed),
                             'time_local_data_guard_enabled': self.get_value(dbs.time_local_data_guard_enabled),
                             'dataguard_region_type': self.get_value(dbs.dataguard_region_type),
                             'customer_contacts': "" if dbs.customer_contacts is None else str(', '.join(x.email for x in dbs.customer_contacts)),
                             'supported_regions_to_clone_to': dbs.supported_regions_to_clone_to,
                             'kms_key_id': self.get_value(dbs.kms_key_id),
                             'vault_id': self.get_value(dbs.vault_id),
                             'key_store_wallet_name': self.get_value(dbs.key_store_wallet_name),
                             'key_store_id': self.get_value(dbs.key_store_id),
                             'available_upgrade_versions': self.get_value(dbs.available_upgrade_versions),
                             'role': self.get_value(dbs.role),
                             'in_memory_percentage': self.get_value(dbs.in_memory_percentage),
                             'in_memory_area_in_gbs': self.get_value(dbs.in_memory_area_in_gbs),
                             'memory_per_oracle_compute_unit_in_gbs': self.get_value(dbs.memory_per_oracle_compute_unit_in_gbs),
                             'next_long_term_backup_time_stamp': self.get_value(dbs.next_long_term_backup_time_stamp),
                             'compute_model': self.get_value(dbs.compute_model),
                             'compute_count': self.get_value(dbs.compute_count),
                             'backup_retention_period_in_days': self.get_value(dbs.backup_retention_period_in_days),
                             'total_backup_storage_size_in_gbs': self.get_value(dbs.total_backup_storage_size_in_gbs),
                             'data_storage_size_in_gbs': self.get_value(dbs.data_storage_size_in_gbs),
                             'used_data_storage_size_in_gbs': self.get_value(dbs.used_data_storage_size_in_gbs),
                             'is_refreshable_clone': self.get_value(dbs.is_refreshable_clone),
                             'time_of_last_refresh': self.get_value(dbs.time_of_last_refresh),
                             'time_of_last_refresh_point': self.get_value(dbs.time_of_last_refresh_point),
                             'time_of_next_refresh': self.get_value(dbs.time_of_next_refresh),
                             'open_mode': self.get_value(dbs.open_mode),
                             'refreshable_status': self.get_value(dbs.refreshable_status),
                             'refreshable_mode': self.get_value(dbs.refreshable_mode),
                             'permission_level': self.get_value(dbs.permission_level),
                             'is_local_data_guard_enabled': self.get_value(dbs.is_local_data_guard_enabled),
                             'is_remote_data_guard_enabled': self.get_value(dbs.is_remote_data_guard_enabled),
                             'is_mtls_connection_required': self.get_value(dbs.is_mtls_connection_required),
                             'time_until_reconnect_clone_enabled': self.get_value(dbs.time_until_reconnect_clone_enabled),
                             'is_auto_scaling_for_storage_enabled': self.get_value(dbs.is_auto_scaling_for_storage_enabled),
                             'allocated_storage_size_in_tbs': self.get_value(dbs.allocated_storage_size_in_tbs),
                             'actual_used_data_storage_size_in_tbs': self.get_value(dbs.actual_used_data_storage_size_in_tbs),
                             'max_cpu_core_count': self.get_value(dbs.max_cpu_core_count),
                             'database_edition': self.get_value(dbs.database_edition),
                             'local_disaster_recovery_type': self.get_value(dbs.local_disaster_recovery_type),
                             'disaster_recovery_region_type': self.get_value(dbs.disaster_recovery_region_type),
                             'time_disaster_recovery_role_changed': self.get_value(dbs.time_disaster_recovery_role_changed),
                             'are_primary_whitelisted_ips_used': self.get_value(dbs.are_primary_whitelisted_ips_used),
                             'autonomous_maintenance_schedule_type': self.get_value(dbs.autonomous_maintenance_schedule_type),
                             'character_set': self.get_value(dbs.character_set),
                             'ncharacter_set': self.get_value(dbs.ncharacter_set),
                             'database_management_status': self.get_value(dbs.database_management_status),
                             'is_access_control_enabled': self.get_value(dbs.is_access_control_enabled),
                             'is_reconnect_clone_enabled': self.get_value(dbs.is_reconnect_clone_enabled),
                             'kms_key_lifecycle_details': self.get_value(dbs.kms_key_lifecycle_details),
                             'kms_key_version_id': self.get_value(dbs.kms_key_version_id),
                             'license_model': self.get_value(dbs.license_model),
                             'local_adg_auto_failover_max_data_loss_limit': self.get_value(dbs.local_adg_auto_failover_max_data_loss_limit),
                             'operations_insights_status': self.get_value(dbs.operations_insights_status),
                             'provisionable_cpus': dbs.provisionable_cpus,
                             'source_id': self.get_value(dbs.source_id),
                             'standby_whitelisted_ips': self.get_value(dbs.standby_whitelisted_ips),
                             'used_data_storage_size_in_tbs': self.get_value(dbs.used_data_storage_size_in_tbs)
                             }

                    # Not included:
                    # apex_details (oci.database.models.AutonomousDatabaseApex)
                    # db_tools_details (list[oci.database.models.DatabaseTool])
                    # key_history_entry (list[oci.database.models.AutonomousDatabaseKeyHistoryEntry])
                    # local_standby_db (oci.database.models.AutonomousDatabaseStandbySummary)
                    # long_term_backup_schedule (oci.database.models.LongTermBackUpScheduleDetails)
                    # remote_disaster_recovery_configuration (oci.database.models.DisasterRecoveryConfiguration)
                    # scheduled_operations (list[oci.database.models.ScheduledOperationDetails])
                    # standby_db (oci.database.models.AutonomousDatabaseStandbySummary)

                    # connection string
                    if dbs.connection_strings:
                        if dbs.connection_strings.all_connection_strings:
                            dbarr = dbs.connection_strings.all_connection_strings
                            value['connection_strings'] = str(', '.join(key + "=" + dbarr[key] for key in dbarr.keys()))

                    # if standby object exist
                    if dbs.standby_db:
                        value['standby_lag_time_in_seconds'] = str(dbs.standby_db.lag_time_in_seconds)
                        value['standby_lifecycle_state'] = str(dbs.standby_db.lifecycle_state)

                    # load bakcups
                    if not self.flags.skip_backups:
                        value['backups'] = self.__load_database_autonomouns_backups(database_client, dbs.id)

                    # license model
                    if dbs.license_model == oci.database.models.AutonomousDatabaseSummary.LICENSE_MODEL_LICENSE_INCLUDED:
                        value['license_model'] = "INCL"
                    elif dbs.license_model == oci.database.models.AutonomousDatabaseSummary.LICENSE_MODEL_BRING_YOUR_OWN_LICENSE:
                        value['license_model'] = "BYOL"
                    else:
                        value['license_model'] = str(dbs.license_model)

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_autonomouns", e, compartment)
            return data

    ##########################################################################
    # __load_database_external_cdb
    ##########################################################################
    def __load_database_external_cdb(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "External CDB Databases"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                list_externals = []
                try:
                    list_externals = oci.pagination.list_call_get_all_results(
                        database_client.list_external_container_databases,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # dbs = oci.database.models.ExternalContainerDatabaseSummary
                for dbs in list_externals:
                    value = {}
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    # management license
                    manage_license = ""
                    if dbs.database_management_config:
                        if dbs.database_management_config.license_model:
                            if "BRING" in dbs.database_management_config.license_model:
                                manage_license = "BYOL"
                            else:
                                manage_license = "INCL"

                    value = {'id': str(dbs.id),
                             'display_name': str(dbs.display_name),
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'lifecycle_details': str(dbs.lifecycle_details),
                             'time_created': str(dbs.time_created),
                             'db_unique_name': str(dbs.db_unique_name),
                             'db_id': str(dbs.db_id),
                             'database_version': str(dbs.database_version),
                             'database_edition': str(dbs.database_edition),
                             'sum_info': "Database External CDB " + ("Managed " + manage_license if manage_license else "Not Managed") + " (Count)",
                             'sum_size_gb': str("1"),
                             'time_zone': str(dbs.time_zone),
                             'character_set': str(dbs.character_set),
                             'ncharacter_set': str(dbs.ncharacter_set),
                             'db_packs': str(dbs.db_packs),
                             'database_configuration': str(dbs.database_configuration),
                             'database_management_status': "" if dbs.database_management_config is None else str(dbs.database_management_config.database_management_status),
                             'database_management_connection_id': "" if dbs.database_management_config is None else str(dbs.database_management_config.database_management_connection_id),
                             'database_management_license_model': "" if dbs.database_management_config is None else str(dbs.database_management_config.license_model),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'region_name': str(self.config['region'])
                             }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_external_cdb", e, compartment)
            return data

    ##########################################################################
    # __load_database_external_pdb
    ##########################################################################
    def __load_database_external_pdb(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "External PDB Databases"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                list_externals = []
                try:
                    list_externals = oci.pagination.list_call_get_all_results(
                        database_client.list_external_pluggable_databases,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # dbs = oci.database.models.ExternalPluggableDatabaseSummary
                for dbs in list_externals:
                    value = {}
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    # management license
                    manage_license = ""
                    if dbs.database_management_config:
                        if dbs.database_management_config.license_model:
                            if "BRING" in dbs.database_management_config.license_model:
                                manage_license = "BYOL"
                            else:
                                manage_license = "INCL"

                    value = {'id': str(dbs.id),
                             'source_id': str(dbs.source_id),
                             'external_container_database_id': str(dbs.external_container_database_id),
                             'display_name': str(dbs.display_name),
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'lifecycle_details': str(dbs.lifecycle_details),
                             'time_created': str(dbs.time_created),
                             'db_unique_name': str(dbs.db_unique_name),
                             'db_id': str(dbs.db_id),
                             'database_version': str(dbs.database_version),
                             'database_edition': str(dbs.database_edition),
                             'sum_info': "Database External PDB " + ("Managed " + manage_license if manage_license else "Not Managed") + " (Count)",
                             'sum_size_gb': str("1"),
                             'time_zone': str(dbs.time_zone),
                             'character_set': str(dbs.character_set),
                             'ncharacter_set': str(dbs.ncharacter_set),
                             'db_packs': str(dbs.db_packs),
                             'database_configuration': str(dbs.database_configuration),
                             'database_management_status': "" if dbs.database_management_config is None else str(dbs.database_management_config.database_management_status),
                             'database_management_connection_id': "" if dbs.database_management_config is None else str(dbs.database_management_config.database_management_connection_id),
                             'database_management_license_model': manage_license,
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'region_name': str(self.config['region'])
                             }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_external_pdb", e, compartment)
            return data

    ##########################################################################
    # __load_database_external_nonpdb
    ##########################################################################
    def __load_database_external_nonpdb(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "External NonPDB Databases"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                list_externals = []
                try:
                    list_externals = oci.pagination.list_call_get_all_results(
                        database_client.list_external_non_container_databases,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # dbs = oci.database.models.ExternalNonContainerDatabaseSummary
                for dbs in list_externals:
                    value = {}
                    if not self.check_lifecycle_state_active(dbs.lifecycle_state):
                        continue

                    # management license
                    manage_license = ""
                    if dbs.database_management_config:
                        if dbs.database_management_config.license_model:
                            if "BRING" in dbs.database_management_config.license_model:
                                manage_license = "BYOL"
                            else:
                                manage_license = "INCL"

                    value = {'id': str(dbs.id),
                             'display_name': str(dbs.display_name),
                             'lifecycle_state': str(dbs.lifecycle_state),
                             'lifecycle_details': str(dbs.lifecycle_details),
                             'time_created': str(dbs.time_created),
                             'db_unique_name': str(dbs.db_unique_name),
                             'db_id': str(dbs.db_id),
                             'database_version': str(dbs.database_version),
                             'database_edition': str(dbs.database_edition),
                             'sum_info': "Database External NonPDB " + ("Managed " + manage_license if manage_license else "Not Managed") + " (Count)",
                             'sum_size_gb': str("1"),
                             'time_zone': str(dbs.time_zone),
                             'character_set': str(dbs.character_set),
                             'ncharacter_set': str(dbs.ncharacter_set),
                             'db_packs': str(dbs.db_packs),
                             'database_configuration': str(dbs.database_configuration),
                             'database_management_status': "" if dbs.database_management_config is None else str(dbs.database_management_config.database_management_status),
                             'database_management_connection_id': "" if dbs.database_management_config is None else str(dbs.database_management_config.database_management_connection_id),
                             'database_management_license_model': "" if dbs.database_management_config is None else str(dbs.database_management_config.license_model),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'defined_tags': [] if dbs.defined_tags is None else dbs.defined_tags,
                             'freeform_tags': [] if dbs.freeform_tags is None else dbs.freeform_tags,
                             'region_name': str(self.config['region'])
                             }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_external_nonpdb", e, compartment)
            return data

    ##########################################################################
    # __load_database_nosql
    ##########################################################################
    def __load_database_nosql(self, nosql_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "NOSQL Databases"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                list_tables = []
                try:
                    list_tables = oci.pagination.list_call_get_all_results(
                        nosql_client.list_tables,
                        compartment['id'],
                        sort_by="name",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        raise

                # loop on auto
                # list_tables = oci.nosql.models.TableCollection
                for tab in list_tables:
                    value = {}
                    if not self.check_lifecycle_state_active(tab.lifecycle_state):
                        continue

                    value = {'id': str(tab.id),
                             'name': str(tab.name),
                             'time_created': str(tab.time_created),
                             'time_updated': str(tab.time_updated),
                             'lifecycle_state': str(tab.lifecycle_state),
                             'lifecycle_details': str(tab.lifecycle_details),
                             'is_auto_reclaimable': str(tab.is_auto_reclaimable),
                             'time_of_expiration': str(tab.time_of_expiration),
                             'sum_info': "NOSQL Database Tables",
                             'sum_size_gb': str("1"),
                             'max_read_units': str(tab.table_limits.max_read_units),
                             'max_write_units': str(tab.table_limits.max_write_units),
                             'max_storage_in_g_bs': str(tab.table_limits.max_storage_in_g_bs),
                             'capacity_mode': str(tab.table_limits.capacity_mode),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'defined_tags': [] if tab.defined_tags is None else tab.defined_tags,
                             'freeform_tags': [] if tab.freeform_tags is None else tab.freeform_tags,
                             'region_name': str(self.config['region'])
                             }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_nosql", e, compartment)
            return data

    ##########################################################################
    # __load_database_mysql
    #   TBD - Backups
    ##########################################################################
    def __load_database_mysql(self, mysql_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "MYSQL Databases"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                databases = []
                try:
                    databases = oci.pagination.list_call_get_all_results(
                        mysql_client.list_db_systems,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                # mysql throw service error often, ignoring incase it does
                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        print("e - " + str(e))
                        return data

                # loop on auto
                # databases = oci.mysql.models.DbSystemSummary
                for mysqls in databases:
                    value = {}
                    if not self.check_lifecycle_state_active(mysqls.lifecycle_state):
                        continue

                    value = {
                        'id': str(mysqls.id),
                        'display_name': str(mysqls.display_name),
                        'description': str(mysqls.description),
                        'is_highly_available': str(mysqls.is_highly_available),
                        'current_placement': str(mysqls.current_placement.availability_domain) if mysqls.current_placement else "",
                        'is_heat_wave_cluster_attached': str(mysqls.is_heat_wave_cluster_attached),
                        'heat_wave_cluster': str(mysqls.heat_wave_cluster.shape_name) + "-" + str(mysqls.heat_wave_cluster.cluster_size) if mysqls.heat_wave_cluster else "",
                        'availability_domain': str(mysqls.availability_domain),
                        'fault_domain': str(mysqls.fault_domain),
                        'endpoints': [],
                        'endpoints_text': str(', '.join(str(x.ip_address) + ":" + str(x.port) for x in mysqls.endpoints)),
                        'lifecycle_state': str(mysqls.lifecycle_state),
                        'mysql_version': str(mysqls.mysql_version),
                        'time_created': str(mysqls.time_created),
                        'time_updated': str(mysqls.time_updated),
                        'deletion_policy': ("Retention: " + str(mysqls.deletion_policy.automatic_backup_retention) + ", Final Backup: " + str(mysqls.deletion_policy.final_backup) + ", Protected: " + str(mysqls.deletion_policy.is_delete_protected)) if mysqls.deletion_policy else "",
                        'shape_name': str(mysqls.shape_name),
                        'shape_ocpu': 0,
                        'shape_memory_gb': 0,
                        'crash_recovery': str(mysqls.crash_recovery),
                        'backup_is_enabled': str(mysqls.backup_policy.is_enabled) if mysqls.backup_policy else "false",
                        'sum_info': 'Database Mysql - ' + str(mysqls.shape_name),
                        'sum_info_storage': 'Database - Storage (GB)',
                        'sum_size_gb': 0,
                        'subnet_id': "",
                        'subnet_name': "",
                        'configuration_id': "",
                        'source': "",
                        'hostname_label': "",
                        'ip_address': "",
                        'port': "",
                        'port_x': "",
                        'channels': "",
                        'maintenance': "",
                        'time_earliest_recovery_point': "",
                        'time_latest_recovery_point': "",
                        'data_storage_size_in_gbs': "",
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'defined_tags': [] if mysqls.defined_tags is None else mysqls.defined_tags,
                        'freeform_tags': [] if mysqls.freeform_tags is None else mysqls.freeform_tags,
                        'region_name': str(self.config['region'])
                    }

                    # get shape
                    if mysqls.shape_name:
                        shape_sizes = self.get_shape_details(str(mysqls.shape_name))
                        if shape_sizes:
                            value['shape_ocpu'] = shape_sizes['cpu']
                            value['shape_memory_gb'] = shape_sizes['memory']

                    # get endpoints
                    for ep in mysqls.endpoints:
                        epval = {
                            'hostname': str(ep.hostname),
                            'ip_address': str(ep.ip_address),
                            'port': str(ep.port),
                            'port_x': str(ep.port_x),
                            'modes': str(', '.join(x for x in ep.modes)),
                            'status': str(ep.status),
                            'status_details': str(ep.status_details)
                        }
                        value['endpoints'].append(epval)

                    try:
                        # get the full DBSystem - oci.mysql.models.DbSystem
                        mysql = mysql_client.get_db_system(mysqls.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                        value['subnet_id'] = str(mysql.subnet_id)
                        value['configuration_id'] = str(mysql.configuration_id)
                        value['data_storage_size_in_gbs'] = str(mysql.data_storage_size_in_gbs)
                        value['sum_size_gb'] = str(mysql.data_storage_size_in_gbs)
                        value['source'] = str(mysql.source) if mysql.source else ""
                        value['hostname_label'] = str(mysql.hostname_label) if mysql.hostname_label else ""
                        value['ip_address'] = str(mysql.ip_address)
                        value['port'] = str(mysql.port)
                        value['port_x'] = str(mysql.port_x)
                        value['maintenance'] = str(mysql.maintenance.window_start_time) if mysql.maintenance else ""
                        value['channels'] = str(', '.join(str(x.display_name) for x in mysql.channels))
                        value['time_earliest_recovery_point'] = str(mysql.point_in_time_recovery_details.time_earliest_recovery_point)[0:16] if mysql.point_in_time_recovery_details else ""
                        value['time_latest_recovery_point'] = str(mysql.point_in_time_recovery_details.time_latest_recovery_point)[0:16] if mysql.point_in_time_recovery_details else ""

                    except Exception:
                        print("w", end="")

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_mysql", e, compartment)
            return data

    ##########################################################################
    # __load_database_software_images
    ##########################################################################
    def __load_database_software_images(self, database_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Database Software Images"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                db_soft_images = []
                try:
                    db_soft_images = oci.pagination.list_call_get_all_results(
                        database_client.list_database_software_images,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        print("e - " + str(e))
                        return data

                # loop on auto
                # array = oci.database.models.DatabaseSoftwareImageSummary
                for array in db_soft_images:
                    if not self.check_lifecycle_state_active(array.lifecycle_state):
                        continue

                    value = {'id': str(array.id),
                             'display_name': str(array.display_name),
                             'database_version': str(array.database_version),
                             'lifecycle_state': str(array.lifecycle_state),
                             'lifecycle_details': str(array.lifecycle_details) if array.lifecycle_details else "",
                             'time_created': str(array.time_created),
                             'image_type': str(array.image_type),
                             'image_shape_family': str(array.image_shape_family),
                             'patch_set': str(array.patch_set),
                             'included_patches_summary': str(array.included_patches_summary),
                             'ls_inventory': str(array.ls_inventory),
                             'is_upgrade_supported': str(array.is_upgrade_supported),
                             'database_software_image_included_patches': array.database_software_image_included_patches,
                             'database_software_image_one_off_patches': array.database_software_image_one_off_patches,
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'defined_tags': [] if array.defined_tags is None else array.defined_tags,
                             'freeform_tags': [] if array.freeform_tags is None else array.freeform_tags,
                             'region_name': str(self.config['region'])
                             }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_software_images", e, compartment)
            return data

    ##########################################################################
    # __load_database_gg_deployments
    ##########################################################################
    def __load_database_gg_deployments(self, gg_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Golden Gate Deployments"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                gg_deployments = []
                try:
                    gg_deployments = oci.pagination.list_call_get_all_results(
                        gg_client.list_deployments,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        print("e - " + str(e))
                        return data

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on auto
                # array = oci.golden_gate.models.DeploymentSummary
                for array in gg_deployments:
                    if not self.check_lifecycle_state_active(array.lifecycle_state):
                        continue

                    value = {'id': str(array.id),
                             'display_name': str(array.display_name),
                             'description': str(array.description),
                             'time_created': str(array.time_created),
                             'time_updated': str(array.time_updated),
                             'lifecycle_state': str(array.lifecycle_state),
                             'lifecycle_details': str(array.lifecycle_details) if array.lifecycle_details else "",
                             'subnet_id': str(array.subnet_id) if array.subnet_id else "",
                             'subnet_name': self.get_network_subnet(str(array.subnet_id), True),
                             'license_model': "BYOL" if array.license_model == "BRING_YOUR_OWN_LICENSE" else "INCL",
                             'fqdn': str(array.fqdn),
                             'cpu_core_count': str(array.cpu_core_count),
                             'is_auto_scaling_enabled': str(array.is_auto_scaling_enabled),
                             'is_public': str(array.is_public),
                             'public_ip_address': str(array.public_ip_address),
                             'private_ip_address': str(array.private_ip_address),
                             'deployment_url': str(array.deployment_url),
                             'is_latest_version': str(array.is_latest_version),
                             'deployment_type': str(array.deployment_type),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'sum_info': "Golden Gate - " + "BYOL" if array.license_model == "BRING_YOUR_OWN_LICENSE" else "INCL",
                             'sum_size_gb': str(array.cpu_core_count),
                             'system_tags': [] if array.system_tags is None else array.system_tags,
                             'defined_tags': [] if array.defined_tags is None else array.defined_tags,
                             'freeform_tags': [] if array.freeform_tags is None else array.freeform_tags,
                             'region_name': str(self.config['region'])
                             }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_gg_deployments", e, compartment)
            return data

    ##########################################################################
    # __load_database_gg_db_registration
    ##########################################################################
    def __load_database_gg_db_registration(self, gg_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Golden Gate DB Reg."
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                db_registrations = []
                try:
                    db_registrations = oci.pagination.list_call_get_all_results(
                        gg_client.list_database_registrations,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    else:
                        print("e - " + str(e))
                        return data

                if self.flags.skip_threads:
                    print(".", end="")

                # loop on auto
                # array = oci.golden_gate.models.DatabaseRegistrationSummary(*
                for array in db_registrations:
                    if not self.check_lifecycle_state_active(array.lifecycle_state):
                        continue

                    value = {'id': str(array.id),
                             'display_name': str(array.display_name),
                             'description': str(array.description),
                             'time_created': str(array.time_created),
                             'time_updated': str(array.time_updated),
                             'lifecycle_state': str(array.lifecycle_state),
                             'lifecycle_details': str(array.lifecycle_details),
                             'subnet_id': str(array.subnet_id),
                             'subnet_name': self.get_network_subnet(str(array.subnet_id), True),
                             'fqdn': str(array.fqdn),
                             'database_id': str(array.database_id),
                             'username': str(array.username),
                             'connection_string': str(array.connection_string),
                             'alias_name': str(array.alias_name),
                             'secret_id': str(array.secret_id),
                             'compartment_name': str(compartment['name']),
                             'compartment_path': str(compartment['path']),
                             'compartment_id': str(compartment['id']),
                             'system_tags': [] if array.system_tags is None else array.system_tags,
                             'defined_tags': [] if array.defined_tags is None else array.defined_tags,
                             'freeform_tags': [] if array.freeform_tags is None else array.freeform_tags,
                             'region_name': str(self.config['region'])
                             }

                    # add the data
                    cnt += 1
                    data.append(value)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_gg_deployments", e, compartment)
            return data

    ##########################################################################
    # __load_database_autonomouns_backups
    ##########################################################################
    def __load_database_autonomouns_backups(self, database_client, db_id):

        data = []
        try:
            backups = oci.pagination.list_call_get_all_results(
                database_client.list_autonomous_database_backups,
                autonomous_database_id=db_id,
                sort_by="TIMECREATED",
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # backup = oci.database.models.AutonomousDatabaseBackupSummary
            for backup in backups:
                if backup.lifecycle_state == oci.database.models.AutonomousDatabaseBackupSummary.LIFECYCLE_STATE_DELETED:
                    continue

                data.append(
                    {'id': str(backup.id),
                     'display_name': str(backup.display_name),
                     'is_automatic': str(backup.is_automatic),
                     'type': str(backup.type),
                     'kms_key_id': str(backup.kms_key_id),
                     'vault_id': str(backup.vault_id),
                     'lifecycle_state': str(backup.lifecycle_state),
                     'lifecycle_details': str(backup.lifecycle_details),
                     'time_started': str(backup.time_started),
                     'time_ended': str(backup.time_ended)
                     })
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
                return data
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_database_autonomouns_backups", e)
            return data

    ##########################################################################
    # __load_container_node_pools
    ##########################################################################
    def __load_container_node_pools(self, container_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "OKE Node Pools"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                try:
                    list_clusters = oci.pagination.list_call_get_all_results(
                        container_client.list_node_pools,
                        compartment['id'],
                        sort_by="NAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.container_engine.models.NodePoolSummary
                for arr in list_clusters:

                    val = {'id': str(arr.id),
                           'name': str(arr.name),
                           'lifecycle_state': str(arr.lifecycle_state),
                           'cluster_id': str(arr.cluster_id),
                           'node_image_id': str(arr.node_image_id),
                           'kubernetes_version': str(arr.kubernetes_version),
                           'node_image_name': str(arr.node_image_name),
                           'node_shape': str(arr.node_shape),
                           'quantity_per_subnet': str(arr.quantity_per_subnet),
                           'subnet_ids': [subnets for subnets in arr.subnet_ids],
                           'node_shape_mem_gb': "",
                           'node_shape_ocpus': "",
                           'node_source_type': "",
                           'node_source_name': "",
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}

                    if arr.node_shape_config:
                        val['node_shape_ocpus'] = arr.node_shape_config.ocpus
                        val['node_shape_mem_gb'] = arr.node_shape_config.memory_in_gbs

                    if arr.node_source:
                        val['node_source_type'] = arr.node_source.source_type
                        val['node_source_name'] = arr.node_source.source_name

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_container_node_pools", e, compartment)
            return data

    ##########################################################################
    # __load_container_clusters
    ##########################################################################
    def __load_container_clusters(self, container_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "OKE Clusters"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                try:
                    list_clusters = oci.pagination.list_call_get_all_results(
                        container_client.list_clusters,
                        compartment['id'],
                        sort_by="NAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.container_engine.models.ClusterSummary
                for arr in list_clusters:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    val = {'id': str(arr.id),
                           'name': str(arr.name),
                           'lifecycle_state': self.get_value(arr.lifecycle_state),
                           'vcn_id': str(arr.vcn_id),
                           'kubernetes_version': self.get_value(arr.kubernetes_version),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'endpoint_is_public_ip_enabled': "",
                           'endpoint_nsg_ids': "",
                           'endpoint_nsg_names': "",
                           'endpoint_subnet_id': "",
                           'endpoint_subnet_name': "",
                           'option_lb_ids': "",
                           'option_network_pods_cidr': "",
                           'option_network_services_cidr': "",
                           'option_is_kubernetes_dashboard_enabled': "",
                           'option_is_tiller_enabled': "",
                           'option_is_pod_security_policy_enabled': "",
                           'time_created': "",
                           'time_deleted': "",
                           'time_updated': "",
                           'created_by_user_id': "",
                           'deleted_by_user_id': "",
                           'updated_by_user_id': "",
                           'endpoint_kubernetes': "",
                           'endpoint_public_endpoint': "",
                           'endpoint_private_endpoint': "",
                           'endpoint_vcn_hostname_endpoint': "",
                           'available_kubernetes_upgrades': str(arr.available_kubernetes_upgrades),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])}

                    # endpoint_config
                    if arr.endpoint_config:
                        val['endpoint_is_public_ip_enabled'] = self.get_value(arr.endpoint_config.is_public_ip_enabled)
                        val['endpoint_subnet_id'] = self.get_value(arr.endpoint_config.subnet_id)
                        if arr.endpoint_config.subnet_id:
                            val['endpoint_subnet_name'] = self.get_network_subnet(arr.endpoint_config.subnet_id)
                        val['endpoint_nsg_ids'] = arr.endpoint_config.nsg_ids
                        if arr.endpoint_config.nsg_ids:
                            val['endpoint_nsg_names'] = self.__load_core_network_get_nsg_names(arr.endpoint_config.nsg_ids)

                    # options
                    if arr.options:
                        val['option_lb_ids'] = arr.options.service_lb_subnet_ids
                        if arr.options.kubernetes_network_config:
                            val['option_network_pods_cidr'] = self.get_value(arr.options.kubernetes_network_config.pods_cidr)
                            val['option_network_services_cidr'] = self.get_value(arr.options.kubernetes_network_config.services_cidr)
                        if arr.options.add_ons:
                            val['option_is_kubernetes_dashboard_enabled'] = self.get_value(arr.options.add_ons.is_kubernetes_dashboard_enabled)
                            val['option_is_tiller_enabled'] = self.get_value(arr.options.add_ons.is_tiller_enabled)
                        if arr.options.admission_controller_options:
                            val['option_is_pod_security_policy_enabled'] = self.get_value(arr.options.admission_controller_options.is_pod_security_policy_enabled)

                    # metadata
                    if arr.metadata:
                        val['time_created'] = self.get_value(arr.metadata.time_created)[0:16]
                        val['time_deleted'] = self.get_value(arr.metadata.time_deleted)[0:16]
                        val['time_updated'] = self.get_value(arr.metadata.time_updated)[0:16]
                        val['created_by_user_id'] = self.get_value(arr.metadata.created_by_user_id)
                        val['deleted_by_user_id'] = self.get_value(arr.metadata.deleted_by_user_id)
                        val['updated_by_user_id'] = self.get_value(arr.metadata.updated_by_user_id)

                    if arr.endpoints:
                        val['endpoint_kubernetes'] = self.get_value(arr.endpoints.kubernetes)
                        val['endpoint_public_endpoint'] = self.get_value(arr.endpoints.public_endpoint)
                        val['endpoint_private_endpoint'] = self.get_value(arr.endpoints.private_endpoint)
                        val['endpoint_vcn_hostname_endpoint'] = self.get_value(arr.endpoints.vcn_hostname_endpoint)

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_container_clusters", e, compartment)
            return data

    ##########################################################################
    # __load_streams_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.streaming.StreamAdminClient(config, **kwargs)
    # class oci.queue.QueueAdminClient(config, **kwargs)
    #
    ##########################################################################
    def __load_section_streams_queues_api_fun_orm_main(self):

        try:
            section_start_time = time.time()
            print("Streams, Queues, API GW, Functions, Resource Management...")

            # initial connection
            stream_client = oci.streaming.StreamAdminClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            queue_client = oci.queue.QueueAdminClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            api_gw_client = oci.apigateway.GatewayClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            api_deployment_client = oci.apigateway.DeploymentClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            function_client = oci.functions.FunctionsManagementClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            orm = oci.resource_manager.ResourceManagerClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                stream_client.base_client.session.proxies = {'https': self.flags.proxy}
                queue_client.base_client.session.proxies = {'https': self.flags.proxy}
                api_gw_client.base_client.session.proxies = {'https': self.flags.proxy}
                api_deployment_client.base_client.session.proxies = {'https': self.flags.proxy}
                function_client.base_client.session.proxies = {'https': self.flags.proxy}
                orm.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_STREAMS, self.C_STREAMS_STREAMS)
            self.__initialize_data_key(self.C_STREAMS, self.C_STREAMS_QUEUES)
            self.__initialize_data_key(self.C_API, self.C_API_GATEWAYS)
            self.__initialize_data_key(self.C_API, self.C_API_DEPLOYMENT)
            self.__initialize_data_key(self.C_FUNCTION, self.C_FUNCTION_APPLICATIONS)
            self.__initialize_data_key(self.C_FUNCTION, self.C_FUNCTION_FUNCTIONS)
            self.__initialize_data_key(self.C_ORM, self.C_ORM_STACKS)

            stream = self.data[self.C_STREAMS]
            apic = self.data[self.C_API]
            fn = self.data[self.C_FUNCTION]
            os = self.data[self.C_ORM]

            ##########################
            # if serial execution
            ##########################
            if self.flags.skip_threads:

                stream[self.C_STREAMS_STREAMS] += self.__load_streams_streams(stream_client, compartments)
                stream[self.C_STREAMS_QUEUES] += self.__load_streams_queues(queue_client, compartments)
                apic[self.C_API_GATEWAYS] += self.__load_api_gateways(api_gw_client, compartments)
                apic[self.C_API_DEPLOYMENT] += self.__load_api_deployments(api_deployment_client, compartments)
                os[self.C_ORM_STACKS] += self.__load_resource_management_stacks(orm, compartments)

                applications = self.__load_functions_applications(function_client, compartments)
                fn[self.C_FUNCTION_APPLICATIONS] += applications
                fn[self.C_FUNCTION_FUNCTIONS] += self.__load_functions_functions(function_client, applications)

            ##########################
            # if parallel execution
            ##########################
            else:
                with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                    future_STREAMS_STREAMS = executor.submit(self.__load_streams_streams, stream_client, compartments)
                    future_STREAMS_QUEUES = executor.submit(self.__load_streams_queues, queue_client, compartments)
                    future_API_GATEWAYS = executor.submit(self.__load_api_gateways, api_gw_client, compartments)
                    future_API_DEPLOYMENT = executor.submit(self.__load_api_deployments, api_deployment_client, compartments)
                    future_ORM_STACKS = executor.submit(self.__load_resource_management_stacks, orm, compartments)
                    future_FUNCTION_APPLICATIONS = executor.submit(self.__load_functions_applications, function_client, compartments)

                    # Wait for application to complete in order to run functions
                    applications = next(as_completed([future_FUNCTION_APPLICATIONS])).result()
                    fn[self.C_FUNCTION_APPLICATIONS] += applications
                    future_FUNCTION_FUNCTIONS = executor.submit(self.__load_functions_functions, function_client, applications)

                    stream[self.C_STREAMS_STREAMS] += next(as_completed([future_STREAMS_STREAMS])).result()
                    stream[self.C_STREAMS_QUEUES] += next(as_completed([future_STREAMS_QUEUES])).result()
                    apic[self.C_API_GATEWAYS] += next(as_completed([future_API_GATEWAYS])).result()
                    apic[self.C_API_DEPLOYMENT] += next(as_completed([future_API_DEPLOYMENT])).result()
                    os[self.C_ORM_STACKS] += next(as_completed([future_ORM_STACKS])).result()
                    fn[self.C_FUNCTION_FUNCTIONS] += next(as_completed([future_FUNCTION_FUNCTIONS])).result()

            self.__load_print_section_time(section_start_time)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_section_streams_queues_api_fun_orm_main", e)

    ##########################################################################
    # __load_streams_streams
    ##########################################################################
    def __load_streams_streams(self, stream_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Streams"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                streams = []
                try:
                    streams = oci.pagination.list_call_get_all_results(
                        stream_client.list_streams, compartment_id=compartment['id'],
                        sort_by="NAME",
                        lifecycle_state=oci.streaming.models.StreamSummary.LIFECYCLE_STATE_ACTIVE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # stream = oci.streaming.models.StreamSummary
                for stream in streams:
                    val = {'id': str(stream.id), 'name': str(stream.name),
                           'partitions': str(stream.partitions), 'time_created': str(stream.time_created),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'messages_endpoint': str(stream.messages_endpoint),
                           'lifecycle_state': str(stream.lifecycle_state),
                           'defined_tags': [] if stream.defined_tags is None else stream.defined_tags,
                           'freeform_tags': [] if stream.freeform_tags is None else stream.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_streams_streams", e, compartment)
            return data

    ##########################################################################
    # __load_queues_queues
    ##########################################################################
    def __load_streams_queues(self, queue_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Queues"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                queues = []
                try:
                    queues = oci.pagination.list_call_get_all_results(
                        queue_client.list_queues, compartment_id=compartment['id'],
                        sort_by="displayName",
                        lifecycle_state=oci.streaming.models.StreamSummary.LIFECYCLE_STATE_ACTIVE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # queue = oci.queue.models.QueueSummary
                for queue_list in queues:
                    queue = queue_client.get_queue(queue_list.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                    val = {
                        'id': str(queue.id),
                        'name': str(queue.display_name),
                        'time_created': str(queue.time_created),
                        'time_updated': str(queue.time_updated),
                        'lifecycle_state': str(queue.lifecycle_state),
                        'lifecycle_details': str(queue.lifecycle_details) if queue.lifecycle_details else "",
                        'retention_in_seconds': str(queue.retention_in_seconds),
                        'visibility_in_seconds': str(queue.visibility_in_seconds),
                        'timeout_in_seconds': str(queue.timeout_in_seconds),
                        'dead_letter_queue_delivery_count': str(queue.dead_letter_queue_delivery_count),
                        'custom_encryption_key_id': str(queue.custom_encryption_key_id) if queue.custom_encryption_key_id else "",
                        'compartment_name': str(compartment['name']),
                        'compartment_id': str(compartment['id']),
                        'compartment_path': str(compartment['path']),
                        'messages_endpoint': str(queue.messages_endpoint),
                        'defined_tags': [] if queue.defined_tags is None else queue.defined_tags,
                        'system_tags': [] if queue.defined_tags is None else queue.defined_tags,
                        'freeform_tags': [] if queue.freeform_tags is None else queue.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_streams_queues", e, compartment)
            return data

    ##########################################################################
    # __load_api_gateways
    ##########################################################################

    def __load_api_gateways(self, api_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "API Gateways"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                apigs = []
                try:
                    apigs = oci.pagination.list_call_get_all_results(
                        api_client.list_gateways,
                        compartment_id=compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_request_error(e):
                        return data

                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # load apis
                for apig in apigs:
                    if not self.check_lifecycle_state_active(apig.lifecycle_state):
                        continue

                    val = {'id': str(apig.id),
                           'display_name': self.get_value(apig.display_name),
                           'endpoint_type': self.get_value(apig.endpoint_type),
                           'hostname': self.get_value(apig.hostname),
                           'subnet_id': self.get_value(apig.subnet_id),
                           'subnet_name': "",
                           'nsg_ids': self.get_value(apig.network_security_group_ids),
                           'nsg_names': str(self.__load_core_network_get_nsg_names(apig.network_security_group_ids)) if apig.network_security_group_ids else "",
                           'time_created': self.get_value(apig.time_created),
                           'time_updated': self.get_value(apig.time_updated),
                           'lifecycle_state': self.get_value(apig.lifecycle_state),
                           'certificate_id': self.get_value(apig.certificate_id),
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'defined_tags': [] if apig.defined_tags is None else apig.defined_tags,
                           'freeform_tags': [] if apig.freeform_tags is None else apig.freeform_tags,
                           'region_name': str(self.config['region']),
                           'deployments': []
                           }

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_api_gateways", e, compartment)
            return data

    ##########################################################################
    # __load_api_deployments
    ##########################################################################

    def __load_api_deployments(self, api_deployment_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "API Deployments"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                apids = []
                try:
                    apids = oci.pagination.list_call_get_all_results(
                        api_deployment_client.list_deployments, compartment_id=compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_request_error(e):
                        return data

                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # load deployment
                for apid in apids:
                    if not self.check_lifecycle_state_active(apid.lifecycle_state):
                        continue

                    val = {'id': str(apid.id),
                           'gateway_id': str(apid.gateway_id),
                           'display_name': str(apid.display_name),
                           'path_prefix': str(apid.path_prefix),
                           'lifecycle_state': str(apid.lifecycle_state),
                           'endpoint': str(apid.endpoint),
                           'time_created': str(apid.time_created),
                           'time_updated': str(apid.time_updated),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if apid.defined_tags is None else apid.defined_tags,
                           'freeform_tags': [] if apid.freeform_tags is None else apid.freeform_tags,
                           'region_name': str(self.config['region']),
                           }

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_api_deployments", e, compartment)
            return data

    ##########################################################################
    # __load_functions_applications
    ##########################################################################
    def __load_functions_applications(self, function_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Function Applications"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                apps = []
                try:
                    apps = oci.pagination.list_call_get_all_results(
                        function_client.list_applications, compartment_id=compartment['id'],
                        sort_by="displayName",
                        lifecycle_state='ACTIVE',
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_request_error(e):
                        return data

                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # fns = oci.functions.models.ApplicationSummary
                for app in apps:
                    val = {'id': str(app.id), 'display_name': str(app.display_name),
                           'subnet_ids': app.subnet_ids, 'time_created': str(app.time_created),
                           'compartment_name': str(compartment['name']), 'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'functions': [],
                           'defined_tags': [] if app.defined_tags is None else app.defined_tags,
                           'freeform_tags': [] if app.freeform_tags is None else app.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_functions_applications", e, compartment)
            return data

    ##########################################################################
    # __load_functions_functions
    ##########################################################################
    def __load_functions_functions(self, function_client, applications):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Functions"
            self.__load_print_status_with_threads(header)

            # loop on all applications
            for app in applications:
                funs = []
                try:
                    funs = oci.pagination.list_call_get_all_results(
                        function_client.list_functions, application_id=app['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_request_error(e):
                        return data

                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print("f", end="")

                # fns = oci.functions.models.ApplicationSummary
                for fun in funs:
                    if not self.check_lifecycle_state_active(fun.lifecycle_state):
                        continue

                    val = {
                        'id': str(fun.id),
                        'display_name': str(fun.display_name),
                        'lifecycle_state': str(fun.lifecycle_state),
                        'image': str(fun.image),
                        'image_digest': str(fun.image_digest),
                        'memory_in_mbs': str(fun.memory_in_mbs),
                        'timeout_in_seconds': str(fun.timeout_in_seconds),
                        'invoke_endpoint': str(fun.invoke_endpoint),
                        'time_created': str(fun.time_created),
                        'time_updated': str(fun.time_updated),
                        'compartment_name': str(app['compartment_name']),
                        'compartment_id': str(fun.compartment_id),
                        'compartment_path': str(app['compartment_path']),
                        'defined_tags': [] if fun.defined_tags is None else fun.defined_tags,
                        'freeform_tags': [] if fun.freeform_tags is None else fun.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)
                    app['functions'].append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_functions_functions", e)
            return data

    ##########################################################################
    # __load_resource_management_stacks
    ##########################################################################
    def __load_resource_management_stacks(self, orm, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "ORM Stacks"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                stacks = []
                try:
                    stacks = oci.pagination.list_call_get_all_results(
                        orm.list_stacks, compartment_id=compartment['id'],
                        lifecycle_state=oci.resource_manager.models.Stack.LIFECYCLE_STATE_ACTIVE,
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # query the stacks
                # stack = oci.resource_manager.models.Stack
                for stack in stacks:
                    val = {'id': str(stack.id),
                           'display_name': self.get_value(stack.display_name),
                           'description': self.get_value(stack.description),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region']),
                           'defined_tags': [] if stack.defined_tags is None else stack.defined_tags,
                           'freeform_tags': [] if stack.freeform_tags is None else stack.freeform_tags,
                           'time_created': str(stack.time_created)}

                    # check jobs
                    try:
                        jobs = oci.pagination.list_call_get_all_results(
                            orm.list_jobs,
                            stack_id=stack.id,
                            sort_by="TIMECREATED",
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning()
                        else:
                            raise

                    # query jobs
                    datajob = []
                    for job in jobs:
                        jobval = {'id': str(job.id),
                                  'display_name': str(job.display_name),
                                  'operation': str(job.operation),
                                  'lifecycle_state': str(job.lifecycle_state),
                                  'time_finished': self.get_value(job.time_finished),
                                  'time_created': self.get_value(job.time_created)}
                        datajob.append(jobval)

                    # add the jobs to the array
                    val['jobs'] = datajob

                    # add the stacks
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_resource_management_stacks", e, compartment)
            return data

    ##########################################################################
    # data load load __load_email_senders
    ##########################################################################
    def __load_email_senders(self, email, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Senders"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                senders = []
                try:
                    senders = oci.pagination.list_call_get_all_results(
                        email.list_senders,
                        compartment['id'],
                        sort_by="EMAILADDRESS",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # query the stacks
                # sender = oci.email.models.Sender
                for sender in senders:
                    val = {'id': str(sender.id),
                           'email_address': self.get_value(sender.email_address),
                           'lifecycle_state': self.get_value(sender.lifecycle_state),
                           'time_created': self.get_value(sender.time_created),
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'defined_tags': [] if sender.defined_tags is None else sender.defined_tags,
                           'freeform_tags': [] if sender.freeform_tags is None else sender.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_email_senders", e, compartment)
            return data

    ##########################################################################
    # data load load __load_email_suppressions
    ##########################################################################
    def __load_email_suppressions(self, email, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:

            errstr = ""
            header = "Suppressions"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # suppressions is only valid in root compartment
                if compartment['id'] != str(self.config['tenancy']):
                    continue

                suppressions = []
                try:
                    suppressions = email.list_suppressions(compartment['id']).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_request_error(e):
                        return data

                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # query the stacks
                # supp = oci.email.models.SuppressionSummary
                for supp in suppressions:
                    val = {'id': str(supp.id),
                           'email_address': self.get_value(supp.email_address),
                           'time_created': self.get_value(supp.time_created),
                           'reason': self.get_value(supp.reason),
                           'compartment_name': str(compartment['name']),
                           'compartment_id': str(compartment['id']),
                           'compartment_path': str(compartment['path']),
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_email_suppressions", e, compartment)
            return data

    ##########################################################################
    # __load_budgets_budgets
    ##########################################################################
    def __load_budgets_budgets(self, budget_client, tenancy_id):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Budgets"
            self.__load_print_status_with_threads(header)

            budgets = []
            try:
                budgets = oci.pagination.list_call_get_all_results(
                    budget_client.list_budgets,
                    tenancy_id,
                    lifecycle_state=oci.budget.models.BudgetSummary.LIFECYCLE_STATE_ACTIVE,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            if self.flags.skip_threads:
                print(".", end="")

            # budget = oci.budget.models.BudgetSummary
            for budget in budgets:
                val = {'id': str(budget.id),
                       'target_compartment_id': str(budget.target_compartment_id),
                       'compartment_name': "",
                       'display_name': str(budget.display_name),
                       'description': str(budget.description),
                       'amount': str(budget.amount),
                       'reset_period': str(budget.reset_period),
                       'alert_rule_count': str(budget.alert_rule_count),
                       'version': str(budget.version),
                       'actual_spend': str(budget.actual_spend),
                       'forecasted_spend': str(budget.forecasted_spend),
                       'time_spend_computed': str(budget.time_spend_computed),
                       'time_created': str(budget.time_created),
                       'time_updated': str(budget.time_updated),
                       'defined_tags': [] if budget.defined_tags is None else budget.defined_tags,
                       'freeform_tags': [] if budget.freeform_tags is None else budget.freeform_tags,
                       'region_name': str(self.config['region'])}

                # fill the comaprtment name
                compartment = self.search_unique_item(self.C_IDENTITY, self.C_IDENTITY_COMPARTMENTS, 'id', str(budget.target_compartment_id))
                if compartment:
                    val['compartment_name'] = compartment['path']

                # add the data
                cnt += 1
                data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_budgets_budgets", e)
            return data

    ##########################################################################
    # __load_monitor_notification_security_quotas_main
    ##########################################################################
    def __load_section_monitor_notification_security_quotas_main(self):

        try:
            section_start_time = time.time()
            print("Monitoring, Notifications, Events, Bastion, Logging, KMS, Limits, Quotas, E-Mail, Budget...")

            monitor_client = oci.monitoring.MonitoringClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            ons_cp_client = oci.ons.NotificationControlPlaneClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            ons_dp_client = oci.ons.NotificationDataPlaneClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            event_client = oci.events.EventsClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            management_agent_client = oci.management_agent.ManagementAgentClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            db_management_client = oci.database_management.DbManagementClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            bs_client = oci.bastion.BastionClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            cg_client = oci.cloud_guard.CloudGuardClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            log_client = oci.logging.LoggingManagementClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            kms_client = oci.key_management.KmsVaultClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            limits_client = oci.limits.LimitsClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            quotas_client = oci.limits.QuotasClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            email_client = oci.email.EmailClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            budget_client = oci.budget.BudgetClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                monitor_client.base_client.session.proxies = {'https': self.flags.proxy}
                ons_cp_client.base_client.session.proxies = {'https': self.flags.proxy}
                ons_dp_client.base_client.session.proxies = {'https': self.flags.proxy}
                event_client.base_client.session.proxies = {'https': self.flags.proxy}
                event_client.base_client.session.proxies = {'https': self.flags.proxy}
                db_management_client.base_client.session.proxies = {'https': self.flags.proxy}
                cg_client.base_client.session.proxies = {'https': self.flags.proxy}
                log_client.base_client.session.proxies = {'https': self.flags.proxy}
                bs_client.base_client.session.proxies = {'https': self.flags.proxy}
                kms_client.base_client.session.proxies = {'https': self.flags.proxy}
                limits_client.base_client.session.proxies = {'https': self.flags.proxy}
                quotas_client.base_client.session.proxies = {'https': self.flags.proxy}
                email_client.base_client.session.proxies = {'https': self.flags.proxy}
                budget_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to tenancy
            tenancy = self.get_tenancy()

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_SECURITY, self.C_SECURITY_BASTION)
            self.__initialize_data_key(self.C_SECURITY, self.C_SECURITY_CLOUD_GUARD)
            self.__initialize_data_key(self.C_SECURITY, self.C_SECURITY_LOGGING_UA)
            self.__initialize_data_key(self.C_SECURITY, self.C_SECURITY_LOGGING)
            self.__initialize_data_key(self.C_SECURITY, self.C_SECURITY_VAULTS)
            self.__initialize_data_key(self.C_MONITORING, self.C_MONITORING_ALARMS)
            self.__initialize_data_key(self.C_MONITORING, self.C_MONITORING_EVENTS)
            self.__initialize_data_key(self.C_MONITORING, self.C_MONITORING_AGENTS)
            self.__initialize_data_key(self.C_MONITORING, self.C_MONITORING_DB_MANAGEMENT)
            self.__initialize_data_key(self.C_NOTIFICATIONS, self.C_NOTIFICATIONS_TOPICS)
            self.__initialize_data_key(self.C_NOTIFICATIONS, self.C_NOTIFICATIONS_SUBSCRIPTIONS)
            self.__initialize_data_key(self.C_LIMITS, self.C_LIMITS_SERVICES)
            self.__initialize_data_key(self.C_LIMITS, self.C_LIMITS_QUOTAS)
            self.__initialize_data_key(self.C_EMAIL, self.C_EMAIL_SENDERS)
            self.__initialize_data_key(self.C_EMAIL, self.C_EMAIL_SUPPRESSIONS)
            self.__initialize_data_key(self.C_BUDGETS, self.C_BUDGETS_BUDGETS)

            monitor = self.data[self.C_MONITORING]
            notifications = self.data[self.C_NOTIFICATIONS]
            sec = self.data[self.C_SECURITY]
            limits = self.data[self.C_LIMITS]
            email = self.data[self.C_EMAIL]
            budget = self.data[self.C_BUDGETS]

            ##########################
            # if serial execution
            ##########################
            if self.flags.skip_threads:
                monitor[self.C_MONITORING_ALARMS] += self.__load_monitoring_alarms(monitor_client, compartments)
                monitor[self.C_MONITORING_EVENTS] += self.__load_monitoring_events(event_client, compartments)
                monitor[self.C_MONITORING_AGENTS] += self.__load_monitoring_agents(management_agent_client, compartments)
                monitor[self.C_MONITORING_DB_MANAGEMENT] += self.__load_monitoring_database_management(db_management_client, compartments)

                notifications[self.C_NOTIFICATIONS_TOPICS] += self.__load_notifications_topics(ons_cp_client, compartments)
                notifications[self.C_NOTIFICATIONS_SUBSCRIPTIONS] += self.__load_notifications_subscriptions(ons_dp_client, compartments)

                sec[self.C_SECURITY_BASTION] += self.__load_security_bastions(bs_client, compartments)
                sec[self.C_SECURITY_LOGGING_UA] += self.__load_security_log_unified_agents(bs_client, compartments)
                sec[self.C_SECURITY_LOGGING] += self.__load_security_log_groups(log_client, compartments)
                sec[self.C_SECURITY_VAULTS] += self.__load_security_kms_vaults(kms_client, compartments)
                sec[self.C_SECURITY_CLOUD_GUARD] += self.__load_security_cloud_guard(cg_client, compartments)

                email[self.C_EMAIL_SENDERS] += self.__load_email_senders(email_client, compartments)
                email[self.C_EMAIL_SUPPRESSIONS] += self.__load_email_suppressions(email_client, compartments)
                budget[self.C_BUDGETS_BUDGETS] += self.__load_budgets_budgets(budget_client, tenancy['id'])

                limits[self.C_LIMITS_SERVICES] += self.__load_limits(limits_client, tenancy['id'], compartments)
                limits[self.C_LIMITS_QUOTAS] += self.__load_quotas(quotas_client, compartments)

            ##########################
            # if parallel execution
            ##########################
            else:
                with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                    future_MONITORING_ALARMS = executor.submit(self.__load_monitoring_alarms, monitor_client, compartments)
                    future_MONITORING_EVENTS = executor.submit(self.__load_monitoring_events, event_client, compartments)
                    future_MONITORING_AGENTS = executor.submit(self.__load_monitoring_agents, management_agent_client, compartments)
                    future_MONITORING_DB_MANAGEMENT = executor.submit(self.__load_monitoring_database_management, db_management_client, compartments)
                    future_NOTIFICATIONS_TOPICS = executor.submit(self.__load_notifications_topics, ons_cp_client, compartments)
                    future_NOTIFICATIONS_SUBSCRIPTIONS = executor.submit(self.__load_notifications_subscriptions, ons_dp_client, compartments)
                    future_SECURITY_BASTION = executor.submit(self.__load_security_bastions, bs_client, compartments)
                    future_SECURITY_LOGGING = executor.submit(self.__load_security_log_groups, log_client, compartments)
                    future_SECURITY_LOGGING_UA = executor.submit(self.__load_security_log_unified_agents, log_client, compartments)
                    future_SECURITY_VAULTS = executor.submit(self.__load_security_kms_vaults, kms_client, compartments)
                    future_SECURITY_CLOUD_GUARD = executor.submit(self.__load_security_cloud_guard, cg_client, compartments)
                    future_EMAIL_SENDERS = executor.submit(self.__load_email_senders, email_client, compartments)
                    future_EMAIL_SUPPRESSIONS = executor.submit(self.__load_email_suppressions, email_client, compartments)
                    future_BUDGETS_BUDGETS = executor.submit(self.__load_budgets_budgets, budget_client, tenancy['id'])
                    future_LIMITS_SERVICES = executor.submit(self.__load_limits, limits_client, tenancy['id'], compartments)
                    future_LIMITS_QUOTAS = executor.submit(self.__load_quotas, quotas_client, compartments)

                    monitor[self.C_MONITORING_ALARMS] += next(as_completed([future_MONITORING_ALARMS])).result()
                    monitor[self.C_MONITORING_EVENTS] += next(as_completed([future_MONITORING_EVENTS])).result()
                    monitor[self.C_MONITORING_AGENTS] += next(as_completed([future_MONITORING_AGENTS])).result()
                    monitor[self.C_MONITORING_DB_MANAGEMENT] += next(as_completed([future_MONITORING_DB_MANAGEMENT])).result()
                    notifications[self.C_NOTIFICATIONS_TOPICS] += next(as_completed([future_NOTIFICATIONS_TOPICS])).result()
                    notifications[self.C_NOTIFICATIONS_SUBSCRIPTIONS] += next(as_completed([future_NOTIFICATIONS_SUBSCRIPTIONS])).result()
                    sec[self.C_SECURITY_BASTION] += next(as_completed([future_SECURITY_BASTION])).result()
                    sec[self.C_SECURITY_LOGGING] += next(as_completed([future_SECURITY_LOGGING])).result()
                    sec[self.C_SECURITY_LOGGING_UA] += next(as_completed([future_SECURITY_LOGGING_UA])).result()
                    sec[self.C_SECURITY_VAULTS] += next(as_completed([future_SECURITY_VAULTS])).result()
                    sec[self.C_SECURITY_CLOUD_GUARD] += next(as_completed([future_SECURITY_CLOUD_GUARD])).result()
                    email[self.C_EMAIL_SENDERS] += next(as_completed([future_EMAIL_SENDERS])).result()
                    email[self.C_EMAIL_SUPPRESSIONS] += next(as_completed([future_EMAIL_SUPPRESSIONS])).result()
                    budget[self.C_BUDGETS_BUDGETS] += next(as_completed([future_BUDGETS_BUDGETS])).result()
                    limits[self.C_LIMITS_SERVICES] += next(as_completed([future_LIMITS_SERVICES])).result()
                    limits[self.C_LIMITS_QUOTAS] += next(as_completed([future_LIMITS_QUOTAS])).result()

            self.__load_print_section_time(section_start_time)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_section_monitor_notification_security_quotas_main", e)

    ##########################################################################
    # __load_monitoring_events
    ##########################################################################
    def __load_monitoring_events(self, event_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Events"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                rules = []
                try:
                    rules = oci.pagination.list_call_get_all_results(
                        event_client.list_rules,
                        compartment['id'],
                        sort_by="DISPLAY_NAME",
                        lifecycle_state="ACTIVE",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # event = oci.events.models.RuleSummary
                for rule in rules:
                    val = {'id': str(rule.id),
                           'display_name': str(rule.display_name),
                           'description': str(rule.description),
                           'condition': str(rule.condition),
                           'is_enabled': str(rule.is_enabled),
                           'time_created': str(rule.time_created),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'actions': [],
                           'defined_tags': [] if rule.defined_tags is None else rule.defined_tags,
                           'freeform_tags': [] if rule.freeform_tags is None else rule.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # get actions using the get_rule
                    try:
                        rule_info = event_client.get_rule(rule.id).data
                        if rule_info:
                            if rule_info.actions:
                                for act in rule_info.actions.actions:
                                    action = {
                                        'id': act.id,
                                        'action_type': str(act.action_type),
                                        'lifecycle_state': str(act.lifecycle_state),
                                        'is_enabled': str(act.is_enabled),
                                        'description': str(act.description),
                                        'dest_id': '',
                                        'dest_name': ''}

                                    if act.action_type == 'ONS':
                                        action['dest_id'] = str(act.topic_id)
                                    if act.action_type == 'OSS':
                                        action['dest_id'] = str(act.stream_id)
                                    if act.action_type == 'FAAS':
                                        action['dest_id'] = str(act.function_id)
                                    val['actions'].append(action)

                    except oci.exceptions.ServiceError:
                        print("w", end="")

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_monitoring_events", e, compartment)
            return data

    ##########################################################################
    # __load_monitoring_agents
    ##########################################################################
    def __load_monitoring_agents(self, management_agent_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Management Agents"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                agents = []
                try:
                    agents = oci.pagination.list_call_get_all_results(
                        management_agent_client.list_management_agents,
                        compartment['id'],
                        sort_by="displayName",
                        lifecycle_state="ACTIVE",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # event = oci.management_agent.models.ManagementAgentSummary
                for agent in agents:
                    val = {'id': str(agent.id),
                           'install_key_id': str(agent.install_key_id),
                           'display_name': str(agent.display_name),
                           'platform_type': str(agent.platform_type),
                           'platform_name': str(agent.platform_name),
                           'platform_version': str(agent.platform_version),
                           'version': str(agent.version),
                           'is_agent_auto_upgradable': str(agent.is_agent_auto_upgradable),
                           'time_created': str(agent.time_created),
                           'host': str(agent.host),
                           'plugin_list': str(', '.join(str(x.plugin_name) for x in agent.plugin_list)),
                           'time_last_heartbeat': str(agent.time_last_heartbeat),
                           'availability_status': str(agent.availability_status),
                           'lifecycle_state': str(agent.lifecycle_state),
                           'lifecycle_details': str(agent.lifecycle_details),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if agent.defined_tags is None else agent.defined_tags,
                           'freeform_tags': [] if agent.freeform_tags is None else agent.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_monitoring_agents", e, compartment)
            return data

    ##########################################################################
    # __load_monitoring_dbmanagement
    ##########################################################################
    def __load_monitoring_database_management(self, db_management_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "DB Management"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                db_managements = []
                try:
                    db_managements = oci.pagination.list_call_get_all_results(
                        db_management_client.list_managed_databases,
                        compartment['id'],
                        sort_by="NAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # event = oci.database_management.models.ManagedDatabase
                for agent in db_managements:
                    val = {'id': str(agent.id),
                           'name': str(agent.name),
                           'database_type': str(agent.database_type),
                           'database_sub_type': str(agent.database_sub_type),
                           'is_cluster': str(agent.is_cluster),
                           'parent_container_id': str(agent.parent_container_id),
                           'time_created': str(agent.time_created),
                           'deployment_type': str(agent.deployment_type),
                           'management_option': str(agent.management_option),
                           'workload_type': str(agent.workload_type),
                           'db_system_id': str(agent.db_system_id),
                           'storage_system_id': str(agent.storage_system_id),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'region_name': str(self.config['region'])
                           }

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_monitoring_database_management", e, compartment)
            return data

    ##########################################################################
    # __load_monitoring_alarms
    ##########################################################################
    def __load_monitoring_alarms(self, monitor_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Alarms"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                alarms = []
                try:
                    alarms = oci.pagination.list_call_get_all_results(
                        monitor_client.list_alarms,
                        compartment['id'],
                        sort_by="displayName",
                        lifecycle_state=oci.monitoring.models.Alarm.LIFECYCLE_STATE_ACTIVE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # alarm = oci.monitoring.models.AlarmSummary
                for alarm in alarms:
                    val = {'id': str(alarm.id),
                           'display_name': str(alarm.display_name),
                           'metric_compartment_id': str(alarm.metric_compartment_id),
                           'namespace': str(alarm.namespace),
                           'query': str(alarm.query),
                           'severity': str(alarm.severity),
                           'destinations': alarm.destinations,
                           'is_enabled': alarm.is_enabled,
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if alarm.defined_tags is None else alarm.defined_tags,
                           'freeform_tags': [] if alarm.freeform_tags is None else alarm.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_monitoring_alarms", e, compartment)
            return data

    ##########################################################################
    # __load_notifications_topics
    ##########################################################################
    def __load_notifications_topics(self, ons_cp_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Topics"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                topics = []
                try:
                    topics = oci.pagination.list_call_get_all_results(
                        ons_cp_client.list_topics,
                        compartment['id'],
                        sort_by="TIMECREATED",
                        lifecycle_state=oci.ons.models.NotificationTopicSummary.LIFECYCLE_STATE_ACTIVE,
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # topic = oci.ons.models.NotificationTopicSummary
                for topic in topics:
                    val = {'topic_id': str(topic.topic_id),
                           'name': str(topic.name),
                           'description': str(topic.description),
                           'time_created': str(topic.time_created),
                           'etag': str(topic.etag),
                           'api_endpoint': str(topic.api_endpoint),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if topic.defined_tags is None else topic.defined_tags,
                           'freeform_tags': [] if topic.freeform_tags is None else topic.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_notifications_topics", e, compartment)
            return data

    ##########################################################################
    # __load_notifications_subscriptions
    ##########################################################################
    def __load_notifications_subscriptions(self, ons_dp_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Subscriptions"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                subs = []
                try:
                    subs = oci.pagination.list_call_get_all_results(
                        ons_dp_client.list_subscriptions,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning("a", False, to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # sub = oci.ons.models.SubscriptionSummary
                for sub in subs:
                    if not self.check_lifecycle_state_active(sub.lifecycle_state):
                        continue

                    val = {'id': str(sub.id),
                           'topic_id': str(sub.topic_id),
                           'protocol': str(sub.protocol),
                           'endpoint': str(sub.endpoint),
                           'created_time': str(sub.created_time),
                           'etag': str(sub.etag),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if sub.defined_tags is None else sub.defined_tags,
                           'freeform_tags': [] if sub.freeform_tags is None else sub.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_notifications_subscriptions", e, compartment)
            return data

    ##########################################################################
    # __load_edge_services_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # class oci.healthchecks.HealthChecksClient(config, **kwargs)
    # class oci.dns.DnsClient(config, **kwargs)
    # class oci.waas.WaasClient(config, **kwargs)
    #
    ##########################################################################
    def __load_section_edge_services_main(self):

        try:
            print("Edge Services...")

            healthcheck_client = oci.healthchecks.HealthChecksClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            dns = oci.dns.DnsClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            waas = oci.waas.WaasClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            waf = oci.waf.WafClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                healthcheck_client.base_client.session.proxies = {'https': self.flags.proxy}
                dns.base_client.session.proxies = {'https': self.flags.proxy}
                waas.base_client.session.proxies = {'https': self.flags.proxy}
                waf.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            # add the key if not exists
            self.__initialize_data_key(self.C_EDGE, self.C_EDGE_HEALTHCHECK_PING)
            self.__initialize_data_key(self.C_EDGE, self.C_EDGE_HEALTHCHECK_HTTP)
            self.__initialize_data_key(self.C_EDGE, self.C_EDGE_DNS_ZONE)
            self.__initialize_data_key(self.C_EDGE, self.C_EDGE_DNS_STEERING)
            self.__initialize_data_key(self.C_EDGE, self.C_EDGE_WAAS_POLICIES)
            self.__initialize_data_key(self.C_EDGE, self.C_EDGE_WAF)

            # reference to stream
            edge = self.data[self.C_EDGE]

            ##########################
            # if serial execution
            ##########################
            if self.flags.skip_threads:
                edge[self.C_EDGE_HEALTHCHECK_PING] += self.__load_edge_healthchecks_ping(healthcheck_client, compartments)
                edge[self.C_EDGE_HEALTHCHECK_HTTP] += self.__load_edge_healthchecks_http(healthcheck_client, compartments)
                edge[self.C_EDGE_DNS_STEERING] += self.__load_edge_dns_steering(dns, compartments)
                edge[self.C_EDGE_WAAS_POLICIES] += self.__load_edge_waas_policies(waas, compartments)
                edge[self.C_EDGE_WAF] += self.__load_edge_waf(waf, compartments)

                # DNS Zone is the slowest API option to skip
                if self.EXCLUDE_DNSZONE not in self.flags.exclude:
                    edge[self.C_EDGE_DNS_ZONE] += self.__load_edge_dns_zone(dns, compartments)

            ##########################
            # if parallel execution
            ##########################
            else:
                with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                    future_EDGE_HEALTHCHECK_PING = executor.submit(self.__load_edge_healthchecks_ping, healthcheck_client, compartments)
                    future_EDGE_HEALTHCHECK_HTTP = executor.submit(self.__load_edge_healthchecks_http, healthcheck_client, compartments)
                    future_EDGE_DNS_STEERING = executor.submit(self.__load_edge_dns_steering, dns, compartments)
                    future_EDGE_WAAS_POLICIES = executor.submit(self.__load_edge_waas_policies, waas, compartments)
                    future_EDGE_WAF = executor.submit(self.__load_edge_waf, waf, compartments)

                    # DNS Zone is the slowest API option to skip
                    if self.EXCLUDE_DNSZONE not in self.flags.exclude:
                        future_EDGE_DNS_ZONE = executor.submit(self.__load_edge_dns_zone, dns, compartments)
                        edge[self.C_EDGE_DNS_ZONE] += next(as_completed([future_EDGE_DNS_ZONE])).result()

                    edge[self.C_EDGE_HEALTHCHECK_PING] += next(as_completed([future_EDGE_HEALTHCHECK_PING])).result()
                    edge[self.C_EDGE_HEALTHCHECK_HTTP] += next(as_completed([future_EDGE_HEALTHCHECK_HTTP])).result()
                    edge[self.C_EDGE_DNS_STEERING] += next(as_completed([future_EDGE_DNS_STEERING])).result()
                    edge[self.C_EDGE_WAAS_POLICIES] += next(as_completed([future_EDGE_WAAS_POLICIES])).result()
                    edge[self.C_EDGE_WAF] += next(as_completed([future_EDGE_WAF])).result()

            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_section_edge_services_main", e)

    ##########################################################################
    # __load_edge_healthchecks_ping
    ##########################################################################
    def __load_edge_healthchecks_ping(self, healthcheck_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Healthcheck Ping"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                healthchecks = []
                try:
                    healthchecks = oci.pagination.list_call_get_all_results(
                        healthcheck_client.list_ping_monitors,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # healthcheck = oci.healthchecks.models.PingMonitorSummary
                for healthcheck in healthchecks:

                    # health = oci.healthchecks.models.PingMonitor
                    # get the proper monitor for more details
                    health = []
                    try:
                        health = healthcheck_client.get_ping_monitor(healthcheck.id).data
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"
                            continue
                        raise
                    val = {'id': str(health.id),
                           'results_url': str(health.results_url),
                           'targets': str(', '.join(x for x in health.targets)),
                           'vantage_point_names': str(', '.join(x for x in health.vantage_point_names)),
                           'port': str(health.port),
                           'timeout_in_seconds': str(health.timeout_in_seconds),
                           'display_name': str(health.display_name),
                           'interval_in_seconds': str(health.interval_in_seconds),
                           'is_enabled': health.is_enabled,
                           'protocol': str(health.protocol),
                           'time_created': str(health.time_created),
                           'lifecycle_state': 'ACTIVE',
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if health.defined_tags is None else health.defined_tags,
                           'freeform_tags': [] if health.freeform_tags is None else health.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_edge_healthchecks_ping", e, compartment)
            return data

    ##########################################################################
    # __load_edge_healthchecks_http
    ##########################################################################
    def __load_edge_healthchecks_http(self, healthcheck_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Healthcheck HTTP"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                healthchecks = []
                try:
                    healthchecks = oci.pagination.list_call_get_all_results(
                        healthcheck_client.list_http_monitors,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise

                if self.flags.skip_threads:
                    print(".", end="")

                # health = oci.healthchecks.models.HttpMonitorSummary
                for healthcheck in healthchecks:

                    # health = oci.healthchecks.models.HttpMonitor
                    # get the proper monitor for more details
                    health = []
                    try:
                        health = healthcheck_client.get_http_monitor(healthcheck.id).data
                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"
                            continue
                        raise
                    except oci.exceptions.ConnectTimeout:
                        self.__load_print_auth_warning()
                        continue

                    val = {'id': str(health.id),
                           'results_url': str(health.results_url),
                           'display_name': str(health.display_name),
                           'interval_in_seconds': str(health.interval_in_seconds),
                           'is_enabled': health.is_enabled,
                           'protocol': str(health.protocol),
                           'method': str(health.method),
                           'path': str(health.path),
                           'targets': str(', '.join(x for x in health.targets)),
                           'vantage_point_names': str(', '.join(x for x in health.vantage_point_names)),
                           'headers': health.headers,
                           'lifecycle_state': 'ACTIVE',
                           'time_created': str(health.time_created),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if health.defined_tags is None else health.defined_tags,
                           'freeform_tags': [] if health.freeform_tags is None else health.freeform_tags,
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_edge_healthchecks_http", e, compartment)
            return data

    ##########################################################################
    # __load_edge_dns_zone
    ##########################################################################
    def __load_edge_dns_zone(self, dns_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "DNS Zone"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        dns_client.list_zones,
                        compartment['id'],
                        lifecycle_state=oci.dns.models.ZoneSummary.LIFECYCLE_STATE_ACTIVE,
                        sort_by="name",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.dns.models.ZoneSummary
                for arr in array:
                    val = {'id': str(arr.id),
                           'name': str(arr.name),
                           'zone_type': str(arr.zone_type),
                           'self_uri': str(arr.self_uri),
                           'time_created': str(arr.time_created),
                           'version': str(arr.version),
                           'serial': str(arr.serial),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_edge_dns_zone", e, compartment)
            return data

    ##########################################################################
    # __load_edge_dns_steering
    ##########################################################################
    def __load_edge_dns_steering(self, dns_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "DNS Steering Policies"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        dns_client.list_steering_policies,
                        compartment['id'],
                        lifecycle_state=oci.dns.models.SteeringPolicySummary.LIFECYCLE_STATE_ACTIVE,
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.dns.models.SteeringPolicySummary
                for arr in array:
                    val = {'id': str(arr.id),
                           'display_name': str(arr.display_name),
                           'ttl': str(arr.ttl),
                           'health_check_monitor_id': str(arr.health_check_monitor_id),
                           'template': str(arr.template),
                           'time_created': str(arr.time_created),
                           'lifecycle_state': str(arr.lifecycle_state),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_edge_dns_zone", e, compartment)
            return data

    ##########################################################################
    # __load_edge_waas_policies
    ##########################################################################
    def __load_edge_waas_policies(self, waas, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "WAAS Policies"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        waas.list_waas_policies,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.waas.models.WaasPolicySummary
                for arr in array:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue
                    val = {'id': str(arr.id),
                           'display_name': str(arr.display_name),
                           'domain': str(arr.domain),
                           'time_created': str(arr.time_created),
                           'lifecycle_state': str(arr.lifecycle_state),
                           'sum_info': "WaaS policies",
                           'sum_size_gb': str("1"),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_edge_waas_policies", e, compartment)
            return data

    ##########################################################################
    # __load_edge_waf
    ##########################################################################
    def __load_edge_waf(self, waf, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "WAF"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        waf.list_web_app_firewalls,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.waf.models.WebAppFirewallSummary
                for arr in array:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue
                    val = {'id': str(arr.id),
                           'display_name': str(arr.display_name),
                           'backend_type': str(arr.backend_type),
                           'web_app_firewall_policy_id': str(arr.web_app_firewall_policy_id),
                           'time_created': str(arr.time_created),
                           'time_updated': str(arr.time_updated),
                           'lifecycle_state': str(arr.lifecycle_state),
                           'sum_info': "Web Application Firewall",
                           'sum_size_gb': str("1"),
                           'compartment_name': str(compartment['name']),
                           'compartment_path': str(compartment['path']),
                           'compartment_id': str(compartment['id']),
                           'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                           'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                           'region_name': str(self.config['region'])
                           }

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_edge_waf", e, compartment)
            return data

    ##########################################################################
    # __load_native_data_ai_main
    ##########################################################################
    def __load_section_native_data_ai_main(self):

        try:
            section_start_time = time.time()
            print("Native, Data and AI ...")

            # For Native
            oic_client = oci.integration.IntegrationInstanceClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            oac_client = oci.analytics.AnalyticsClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            oce_client = oci.oce.OceInstanceClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            ocvs_client = oci.ocvp.SddcClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            esxi_client = oci.ocvp.EsxiHostClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            vb_client = oci.visual_builder.VbInstanceClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            opensearch_client = oci.opensearch.OpensearchClusterClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            virtual_network = oci.core.VirtualNetworkClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            devops_client = oci.devops.DevopsClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            ds_client = oci.data_science.DataScienceClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            dc_client = oci.data_catalog.DataCatalogClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            df_client = oci.data_flow.DataFlowClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            oda_client = oci.oda.OdaClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            bds_client = oci.bds.BdsClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            di_client = oci.data_integration.DataIntegrationClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                oic_client.base_client.session.proxies = {'https': self.flags.proxy}
                oac_client.base_client.session.proxies = {'https': self.flags.proxy}
                oce_client.base_client.session.proxies = {'https': self.flags.proxy}
                ocvs_client.base_client.session.proxies = {'https': self.flags.proxy}
                vb_client.base_client.session.proxies = {'https': self.flags.proxy}
                esxi_client.base_client.session.proxies = {'https': self.flags.proxy}
                virtual_network.base_client.session.proxies = {'https': self.flags.proxy}
                opensearch_client.base_client.session.proxies = {'https': self.flags.proxy}
                devops_client.base_client.session.proxies = {'https': self.flags.proxy}

                ds_client.base_client.session.proxies = {'https': self.flags.proxy}
                dc_client.base_client.session.proxies = {'https': self.flags.proxy}
                df_client.base_client.session.proxies = {'https': self.flags.proxy}
                oda_client.base_client.session.proxies = {'https': self.flags.proxy}
                bds_client.base_client.session.proxies = {'https': self.flags.proxy}
                di_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            compartments = self.get_compartment()

            self.__initialize_data_key(self.C_PAAS_NATIVE, self.C_PAAS_NATIVE_OAC)
            self.__initialize_data_key(self.C_PAAS_NATIVE, self.C_PAAS_NATIVE_OIC)
            self.__initialize_data_key(self.C_PAAS_NATIVE, self.C_PAAS_NATIVE_OCE)
            self.__initialize_data_key(self.C_PAAS_NATIVE, self.C_PAAS_NATIVE_OCVS)
            self.__initialize_data_key(self.C_PAAS_NATIVE, self.C_PAAS_NATIVE_VB)
            self.__initialize_data_key(self.C_PAAS_NATIVE, self.C_PAAS_NATIVE_DEVOPS)
            self.__initialize_data_key(self.C_PAAS_NATIVE, self.C_PAAS_NATIVE_OPEN_SEARCH)

            self.__initialize_data_key(self.C_DATA_AI, self.C_DATA_AI_CATALOG)
            self.__initialize_data_key(self.C_DATA_AI, self.C_DATA_AI_DCREGISTRY)
            self.__initialize_data_key(self.C_DATA_AI, self.C_DATA_AI_FLOW)
            self.__initialize_data_key(self.C_DATA_AI, self.C_DATA_AI_SCIENCE)
            self.__initialize_data_key(self.C_DATA_AI, self.C_DATA_AI_ODA)
            self.__initialize_data_key(self.C_DATA_AI, self.C_DATA_AI_DI)
            self.__initialize_data_key(self.C_DATA_AI, self.C_DATA_AI_BDS)

            ##########################
            # if serial execution
            ##########################
            if self.flags.skip_threads:
                paas = self.data[self.C_PAAS_NATIVE]
                paas[self.C_PAAS_NATIVE_OCVS] += self.__load_paas_ocvs(ocvs_client, esxi_client, virtual_network, compartments)
                paas[self.C_PAAS_NATIVE_OIC] += self.__load_paas_oic(oic_client, compartments)
                paas[self.C_PAAS_NATIVE_OCE] += self.__load_paas_oce(oce_client, compartments)
                paas[self.C_PAAS_NATIVE_OAC] += self.__load_paas_oac(oac_client, compartments)
                paas[self.C_PAAS_NATIVE_VB] += self.__load_paas_visualbuilder(vb_client, compartments)
                paas[self.C_PAAS_NATIVE_DEVOPS] += self.__load_paas_devops(devops_client, compartments)
                paas[self.C_PAAS_NATIVE_OPEN_SEARCH] += self.__load_paas_open_search(opensearch_client, compartments)

                data_ai = self.data[self.C_DATA_AI]
                data_ai[self.C_DATA_AI_CATALOG] += self.__load_data_ai_catalog(dc_client, compartments)
                data_ai[self.C_DATA_AI_FLOW] += self.__load_data_ai_flow(df_client, compartments)
                data_ai[self.C_DATA_AI_SCIENCE] += self.__load_data_ai_science(ds_client, compartments)
                data_ai[self.C_DATA_AI_ODA] += self.__load_data_ai_oda(oda_client, compartments)
                data_ai[self.C_DATA_AI_BDS] += self.__load_data_ai_bds(bds_client, compartments)
                data_ai[self.C_DATA_AI_DI] += self.__load_data_ai_data_integration(di_client, compartments)

            ##########################
            # if parallel execution
            ##########################
            else:
                with ThreadPoolExecutor(max_workers=self.flags.threads) as executor:
                    future_PAAS_NATIVE_OCVS = executor.submit(self.__load_paas_ocvs, ocvs_client, esxi_client, virtual_network, compartments)
                    future_PAAS_NATIVE_OIC = executor.submit(self.__load_paas_oic, oic_client, compartments)
                    future_PAAS_NATIVE_OCE = executor.submit(self.__load_paas_oce, oce_client, compartments)
                    future_PAAS_NATIVE_OAC = executor.submit(self.__load_paas_oac, oac_client, compartments)
                    future_PAAS_NATIVE_VB = executor.submit(self.__load_paas_visualbuilder, vb_client, compartments)
                    future_PAAS_NATIVE_DEVOPS = executor.submit(self.__load_paas_devops, devops_client, compartments)
                    future_PAAS_NATIVE_OPEN_SEARCH = executor.submit(self.__load_paas_open_search, opensearch_client, compartments)

                    future_DATA_AI_CATALOG = executor.submit(self.__load_data_ai_catalog, dc_client, compartments)
                    future_DATA_AI_FLOW = executor.submit(self.__load_data_ai_flow, df_client, compartments)
                    future_DATA_AI_SCIENCE = executor.submit(self.__load_data_ai_science, ds_client, compartments)
                    future_DATA_AI_ODA = executor.submit(self.__load_data_ai_oda, oda_client, compartments)
                    future_DATA_AI_BDS = executor.submit(self.__load_data_ai_bds, bds_client, compartments)
                    future_DATA_AI_DI = executor.submit(self.__load_data_ai_data_integration, di_client, compartments)

                    paas = self.data[self.C_PAAS_NATIVE]
                    paas[self.C_PAAS_NATIVE_OCVS] += next(as_completed([future_PAAS_NATIVE_OCVS])).result()
                    paas[self.C_PAAS_NATIVE_OIC] += next(as_completed([future_PAAS_NATIVE_OIC])).result()
                    paas[self.C_PAAS_NATIVE_OCE] += next(as_completed([future_PAAS_NATIVE_OCE])).result()
                    paas[self.C_PAAS_NATIVE_OAC] += next(as_completed([future_PAAS_NATIVE_OAC])).result()
                    paas[self.C_PAAS_NATIVE_VB] += next(as_completed([future_PAAS_NATIVE_VB])).result()
                    paas[self.C_PAAS_NATIVE_DEVOPS] += next(as_completed([future_PAAS_NATIVE_DEVOPS])).result()
                    paas[self.C_PAAS_NATIVE_OPEN_SEARCH] += next(as_completed([future_PAAS_NATIVE_OPEN_SEARCH])).result()

                    data_ai = self.data[self.C_DATA_AI]
                    data_ai[self.C_DATA_AI_CATALOG] += next(as_completed([future_DATA_AI_CATALOG])).result()
                    data_ai[self.C_DATA_AI_FLOW] += next(as_completed([future_DATA_AI_FLOW])).result()
                    data_ai[self.C_DATA_AI_SCIENCE] += next(as_completed([future_DATA_AI_SCIENCE])).result()
                    data_ai[self.C_DATA_AI_ODA] += next(as_completed([future_DATA_AI_ODA])).result()
                    data_ai[self.C_DATA_AI_BDS] += next(as_completed([future_DATA_AI_BDS])).result()
                    data_ai[self.C_DATA_AI_DI] += next(as_completed([future_DATA_AI_DI])).result()

            self.__load_print_section_time(section_start_time)
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_section_native_data_ai_main", e)

    ##########################################################################
    # __load_data_ai_catalog
    ##########################################################################
    def __load_data_ai_catalog(self, dc_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Data Catalog"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        dc_client.list_catalogs,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.data_catalog.models.CatalogSummary
                for arr in array:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    val = {
                        'id': str(arr.id),
                        'display_name': self.get_value(arr.display_name),
                        'time_created': self.get_value(arr.time_created),
                        'time_updated': self.get_value(arr.time_updated),
                        'number_of_objects': self.get_value(arr.number_of_objects),
                        'lifecycle_state': self.get_value(arr.lifecycle_state),
                        'lifecycle_details': self.get_value(arr.lifecycle_details),
                        'attached_catalog_private_endpoints': str(', '.join(x for x in arr.attached_catalog_private_endpoints)) if arr.attached_catalog_private_endpoints else "",
                        'sum_info': "Data Catalog",
                        'sum_size_gb': str("1"),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_data_ai_catalog", e, compartment)
            return data

    ##########################################################################
    # __load_data_ai_science
    ##########################################################################
    def __load_data_ai_science(self, ds_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Data Science"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        ds_client.list_projects,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.data_science.models.ProjectSummary
                for arr in array:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    val = {
                        'id': str(arr.id),
                        'display_name': self.get_value(arr.display_name),
                        'time_created': self.get_value(arr.time_created),
                        'description': self.get_value(arr.description),
                        'created_by': self.get_value(arr.created_by),
                        'lifecycle_state': self.get_value(arr.lifecycle_state),
                        'sum_info': "Data Science",
                        'sum_size_gb': str("1"),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_data_ai_science", e, compartment)
            return data

    ##########################################################################
    # __load_data_ai_flow
    ##########################################################################
    def __load_data_ai_flow(self, df_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Data Flow"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        df_client.list_applications,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.data_flow.models.ApplicationSummary
                for arr in array:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    val = {
                        'id': str(arr.id),
                        'display_name': self.get_value(arr.display_name),
                        'time_created': self.get_value(arr.time_created),
                        'time_updated': self.get_value(arr.time_updated),
                        'language': self.get_value(arr.language),
                        'lifecycle_state': self.get_value(arr.lifecycle_state),
                        'owner_principal_id': self.get_value(arr.owner_principal_id),
                        'owner_user_name': self.get_value(arr.owner_user_name),
                        'spark_version': self.get_value(arr.spark_version),
                        'type': self.get_value(arr.type),
                        'sum_info': "Data Flow",
                        'sum_size_gb': str("1"),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_data_ai_flow", e, compartment)
            return data

    ##########################################################################
    # __load_data_ai_oda
    ##########################################################################
    def __load_data_ai_oda(self, oda_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Data Assistant"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                odas = []
                try:
                    odas = oci.pagination.list_call_get_all_results(
                        oda_client.list_oda_instances,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # oda = oci.oda.models.OdaInstanceSummary
                for oda in odas:
                    if not self.check_lifecycle_state_active(oda.lifecycle_state):
                        continue
                    val = {
                        'id': str(oda.id),
                        'display_name': self.get_value(oda.display_name),
                        'description': self.get_value(oda.description),
                        'shape_name': self.get_value(oda.shape_name),
                        'time_created': self.get_value(oda.time_created),
                        'time_updated': self.get_value(oda.time_updated),
                        'lifecycle_state': self.get_value(oda.lifecycle_state),
                        'lifecycle_sub_state': self.get_value(oda.lifecycle_sub_state),
                        'state_message': self.get_value(oda.state_message),
                        'is_role_based_access': self.get_value(oda.is_role_based_access),
                        'identity_domain': self.get_value(oda.identity_domain),
                        'imported_package_names': str(', '.join(x for x in oda.imported_package_names)) if oda.imported_package_names else "",
                        'attachment_types': str(', '.join(x for x in oda.attachment_types)) if oda.attachment_types else "",
                        'sum_info': "Digital Assistant " + str(oda.shape_name),
                        'sum_size_gb': str("1"),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'defined_tags': [] if oda.defined_tags is None else oda.defined_tags,
                        'freeform_tags': [] if oda.freeform_tags is None else oda.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_data_ai_oda", e, compartment)
            return data

    ##########################################################################
    # __load_data_ai_bds
    ##########################################################################
    def __load_data_ai_bds(self, bds_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Big Data Service"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                bdss = []
                try:
                    bdss = oci.pagination.list_call_get_all_results(
                        bds_client.list_bds_instances,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                # TBD: don't add warning count until GA on the service
                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning("a", False, to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning("a", False, to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # bds = bds.models.BdsInstanceSummary
                for bds in bdss:
                    if not self.check_lifecycle_state_active(bds.lifecycle_state):
                        continue

                    val = {
                        'id': str(bds.id),
                        'display_name': self.get_value(bds.display_name),
                        'number_of_nodes': self.get_value(bds.number_of_nodes),
                        'cluster_version': self.get_value(bds.cluster_version),
                        'is_high_availability': self.get_value(bds.is_high_availability),
                        'is_secure': self.get_value(bds.is_secure),
                        'cluster_profile': self.get_value(bds.cluster_profile),
                        'lifecycle_state': self.get_value(bds.lifecycle_state),
                        'is_cloud_sql_configured': self.get_value(bds.is_cloud_sql_configured),
                        'time_created': self.get_value(bds.time_created),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'sum_info': "Big Data Service (Nodes)",
                        'sum_size_gb': self.get_value(bds.number_of_nodes),
                        'number_of_nodes_requiring_maintenance_reboot': self.get_value(bds.number_of_nodes_requiring_maintenance_reboot),
                        'is_kafka_configured': self.get_value(bds.is_kafka_configured),
                        'defined_tags': [] if bds.defined_tags is None else bds.defined_tags,
                        'freeform_tags': [] if bds.freeform_tags is None else bds.freeform_tags,
                        'error_message': "",
                        'network_cidr_block': "",
                        'network_is_nat_gateway_required': "",
                        'cluster_details_bda_version': "",
                        'cluster_details_bdm_version': "",
                        'cluster_details_bds_version': "",
                        'cluster_details_os_version': "",
                        'cluster_details_db_version': "",
                        'cluster_details_bd_cell_version': "",
                        'cluster_details_csql_cell_version': "",
                        'cluster_details_time_refreshed': "",
                        'cluster_details_c_manager_url': "",
                        'cluster_details_ambari_url': "",
                        'cluster_details_big_data_manager_url': "",
                        'cluster_details_hue_server_url': "",
                        'cluster_details_odh_version': "",
                        'cluster_details_jupyter_hub_url': "",
                        'cloud_sql_details_shape': "",
                        'cloud_sql_details_block_volume_size_in_gbs': "",
                        'cloud_sql_details_is_kerberos_mapped_to_database_users': "",
                        'cloud_sql_details_ip_address': "",
                        'created_by': "",
                        'kms_key_id': "",
                        'nodes': [],
                        'autoscale': [],
                        'region_name': str(self.config['region'])}

                    # Get extra details
                    try:
                        # bds.models.BdsInstance
                        ext = bds_client.get_bds_instance(
                            bds.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                        if ext:
                            if ext.network_config:
                                val['network_cidr_block'] = self.get_value(ext.network_config.cidr_block)
                                val['network_is_nat_gateway_required'] = self.get_value(ext.network_config.is_nat_gateway_required)

                            if ext.cluster_details:
                                val['cluster_details_bda_version'] = self.get_value(ext.cluster_details.bda_version)
                                val['cluster_details_bdm_version'] = self.get_value(ext.cluster_details.bdm_version)
                                val['cluster_details_bds_version'] = self.get_value(ext.cluster_details.bds_version)
                                val['cluster_details_os_version'] = self.get_value(ext.cluster_details.os_version)
                                val['cluster_details_db_version'] = self.get_value(ext.cluster_details.db_version)
                                val['cluster_details_bd_cell_version'] = self.get_value(ext.cluster_details.bd_cell_version)
                                val['cluster_details_csql_cell_version'] = self.get_value(ext.cluster_details.csql_cell_version)
                                val['cluster_details_time_refreshed'] = self.get_value(ext.cluster_details.time_refreshed)
                                val['cluster_details_c_manager_url'] = self.get_value(ext.cluster_details.cloudera_manager_url)
                                val['cluster_details_ambari_url'] = self.get_value(ext.cluster_details.ambari_url)
                                val['cluster_details_big_data_manager_url'] = self.get_value(ext.cluster_details.big_data_manager_url)
                                val['cluster_details_hue_server_url'] = self.get_value(ext.cluster_details.hue_server_url)
                                val['cluster_details_odh_version'] = self.get_value(ext.cluster_details.odh_version)
                                val['cluster_details_jupyter_hub_url'] = self.get_value(ext.cluster_details.jupyter_hub_url)

                            nodes = []
                            for nd in ext.nodes:
                                nodes.append({
                                    'instance_id': self.get_value(nd.instance_id),
                                    'display_name': self.get_value(nd.display_name),
                                    'lifecycle_state': self.get_value(nd.lifecycle_state),
                                    'node_type': self.get_value(nd.node_type),
                                    'shape': self.get_value(nd.shape),
                                    'subnet_id': self.get_value(nd.subnet_id),
                                    'subnet_name': self.get_network_subnet(nd.subnet_id, False),
                                    'subnet_name_detailed': self.get_network_subnet(nd.subnet_id, True),
                                    'ip_address': self.get_value(nd.ip_address),
                                    'hostname': self.get_value(nd.hostname),
                                    'image_id': self.get_value(nd.image_id),
                                    'availability_domain': self.get_value(nd.availability_domain),
                                    'fault_domain': self.get_value(nd.fault_domain),
                                    'time_created': self.get_value(nd.time_created),
                                    'time_updated': self.get_value(nd.time_updated),
                                    'ocpus': self.get_value(nd.ocpus),
                                    'memory_in_gbs': self.get_value(nd.memory_in_gbs),
                                    'nvmes': self.get_value(nd.nvmes),
                                    'attached_block_volumes_ids': [bd.volume_attachment_id for bd in nd.attached_block_volumes],
                                    'attached_block_volumes_gbs': [bd.volume_size_in_gbs for bd in nd.attached_block_volumes],
                                    'local_disks_total_size_in_gbs': self.get_value(nd.local_disks_total_size_in_gbs),
                                    'time_maintenance_reboot_due': self.get_value(nd.time_maintenance_reboot_due)})

                            # Added the nodes to the main array
                            val['nodes'] = nodes
                            if ext.cloud_sql_details:
                                val['cloud_sql_details_shape'] = self.get_value(ext.cloud_sql_details.shape)
                                val['cloud_sql_details_block_volume_size_in_gbs'] = self.get_value(ext.cloud_sql_details.block_volume_size_in_gbs)
                                val['cloud_sql_details_is_kerberos_mapped_to_database_users'] = self.get_value(ext.cloud_sql_details.is_kerberos_mapped_to_database_users)
                                val['cloud_sql_details_ip_address'] = self.get_value(ext.cloud_sql_details.ip_address)
                            val['created_by'] = self.get_value(ext.created_by)
                            val['kms_key_id'] = self.get_value(ext.kms_key_id)

                    except Exception as e:
                        errstr += "Issue with " + str(bds.display_name) + " "
                        val['error_message'] = str(e)
                        self.__load_print_auth_warning("", True, to_print=self.flags.skip_threads)

                    # get Autoscale configuration
                    try:
                        # bds.models.BdsInstance
                        ext = bds_client.list_auto_scaling_configurations(
                            compartment_id=bds.compartment_id,
                            bds_instance_id=bds.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data

                        autoscale = []
                        for ats in ext:
                            autoscale.append({
                                'display_name': self.get_value(ats.display_name),
                                'lifecycle_state': self.get_value(ats.lifecycle_state),
                                'node_type': self.get_value(ats.node_type),
                                'time_created': self.get_value(ats.time_created),
                                'time_updated': self.get_value(ats.time_updated),
                                'policy_type': self.get_value(ats.policy_details.policy_type) if ats.policy_details else "",
                                'policy_trigger_type': self.get_value(ats.policy_details.trigger_type) if ats.policy_details else "",
                                'policy_action_type': self.get_value(ats.policy_details.action_type) if ats.policy_details else "",
                            })
                        val['autoscale'] = autoscale

                    except Exception as e:
                        errstr += "Issue with " + str(bds.display_name) + " Autoscale "
                        val['error_message'] = str(e)
                        self.__load_print_auth_warning("", True, to_print=self.flags.skip_threads)

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_data_ai_bds", e, compartment)
            return data

    ##########################################################################
    # __load_data_ai_data_integration
    ##########################################################################
    def __load_data_ai_data_integration(self, di_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Data Integration"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                dis = []
                try:
                    dis = oci.pagination.list_call_get_all_results(
                        di_client.list_workspaces,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning("a", False, to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning("a", False, to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # di = oci.data_integration.models.WorkspaceSummary
                for di in dis:
                    if not self.check_lifecycle_state_active(di.lifecycle_state):
                        continue

                    val = {
                        'id': str(di.id),
                        'description': self.get_value(di.description),
                        'display_name': self.get_value(di.display_name),
                        'lifecycle_state': self.get_value(di.lifecycle_state),
                        'time_created': self.get_value(di.time_created),
                        'time_updated': self.get_value(di.time_updated),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'sum_info': "Data Integration (Workspaces)",
                        'sum_size_gb': str(1),
                        'defined_tags': [] if di.defined_tags is None else di.defined_tags,
                        'freeform_tags': [] if di.freeform_tags is None else di.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_data_ai_data_integration", e, compartment)
            return data

    ##########################################################################
    # __load_paas_oic
    ##########################################################################
    def __load_paas_oic(self, oic_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "OIC Native"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                oics = []
                try:
                    oics = oci.pagination.list_call_get_all_results(
                        oic_client.list_integration_instances,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # oic = oci.integration.models.IntegrationInstanceSummary
                for oic in oics:
                    if not self.check_lifecycle_state_active(oic.lifecycle_state):
                        continue

                    val = {
                        'id': str(oic.id),
                        'display_name': str(oic.display_name),
                        'integration_instance_type': str(oic.integration_instance_type),
                        'time_created': str(oic.time_created),
                        'time_updated': str(oic.time_updated),
                        'lifecycle_state': str(oic.lifecycle_state),
                        'state_message': str(oic.state_message),
                        'instance_url': str(oic.instance_url),
                        'message_packs': str(oic.message_packs),
                        'is_byol': oic.is_byol,
                        'sum_info': "PaaS OIC Native " + ("BYOL" if oic.is_byol else "INCL") + " - Msg Pack",
                        'sum_size_gb': str(oic.message_packs),
                        'is_file_server_enabled': str(oic.is_file_server_enabled),
                        'is_visual_builder_enabled': str(oic.is_visual_builder_enabled),
                        'shape': str(oic.shape),
                        'network_endpoint_type': "",
                        'consumption_model': str(oic.consumption_model),
                        'defined_tags': [] if oic.defined_tags is None else oic.defined_tags,
                        'freeform_tags': [] if oic.freeform_tags is None else oic.freeform_tags,
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])}

                    # end point
                    if oic.network_endpoint_details:
                        val['network_endpoint_type'] = str(oic.network_endpoint_details.network_endpoint_type)

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_paas_oic", e, compartment)
            return data

    ##########################################################################
    # __load_paas_osvc - vmware
    ##########################################################################
    def __load_paas_ocvs(self, ocvs_client, esxi_client, virtual_network, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "OCVS Native - VMWare"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                ocvs = []
                try:
                    ocvs = oci.pagination.list_call_get_all_results(
                        ocvs_client.list_sddcs,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # vmware_summary = oci.ocvp.models.SddcSummary
                for vmware_summary in ocvs:
                    if not self.check_lifecycle_state_active(vmware_summary.lifecycle_state):
                        continue

                    # get vmware object with more details
                    # vmware = oci.ocvp.models.Sddc
                    vmware = ocvs_client.get_sddc(vmware_summary.id).data

                    val = {
                        'id': str(vmware.id),
                        'display_name': str(vmware.display_name),
                        'compute_availability_domain': str(vmware.compute_availability_domain),
                        'instance_display_name_prefix': str(vmware.instance_display_name_prefix),
                        'vmware_software_version': str(vmware.vmware_software_version),
                        'esxi_hosts_count': str(vmware.esxi_hosts_count),
                        'nsx_manager_fqdn': str(vmware.nsx_manager_fqdn),
                        'nsx_manager_private_ip_id': str(vmware.nsx_manager_private_ip_id),
                        'nsx_manager_private_ip': self.__load_core_network_single_privateip(virtual_network, vmware.nsx_manager_private_ip_id, False),
                        'nsx_manager_username': str(vmware.nsx_manager_username),
                        'nsx_manager_initial_password': str(vmware.nsx_manager_initial_password),
                        'vcenter_fqdn': str(vmware.vcenter_fqdn),
                        'vcenter_username': str(vmware.vcenter_username),
                        'vcenter_private_ip_id': str(vmware.vcenter_private_ip_id),
                        'vcenter_private_ip': self.__load_core_network_single_privateip(virtual_network, vmware.vcenter_private_ip_id, False),
                        'vcenter_initial_password': str(vmware.vcenter_initial_password),
                        'workload_network_cidr': str(vmware.workload_network_cidr),
                        'nsx_overlay_segment_name': str(vmware.nsx_overlay_segment_name),
                        'nsx_edge_uplink_ip_id': str(vmware.nsx_edge_uplink_ip_id),
                        'nsx_edge_uplink_ip': self.__load_core_network_single_privateip(virtual_network, vmware.nsx_edge_uplink_ip_id, True),
                        'provisioning_subnet_id': str(vmware.provisioning_subnet_id),
                        'provisioning_subnet': self.get_network_subnet(vmware.provisioning_subnet_id, True),
                        'vsphere_vlan_id': str(vmware.vsphere_vlan_id),
                        'vsphere_vlan': self.__load_core_network_single_vlan(virtual_network, vmware.vsphere_vlan_id),
                        'vmotion_vlan_id': str(vmware.vmotion_vlan_id),
                        'vmotion_vlan': self.__load_core_network_single_vlan(virtual_network, vmware.vmotion_vlan_id),
                        'vsan_vlan_id': str(vmware.vsan_vlan_id),
                        'vsan_vlan': self.__load_core_network_single_vlan(virtual_network, vmware.vsan_vlan_id),
                        'nsx_v_tep_vlan_id': str(vmware.nsx_v_tep_vlan_id),
                        'nsx_v_tep_vlan': self.__load_core_network_single_vlan(virtual_network, vmware.nsx_v_tep_vlan_id),
                        'nsx_edge_v_tep_vlan_id': str(vmware.nsx_edge_v_tep_vlan_id),
                        'nsx_edge_v_tep_vlan': self.__load_core_network_single_vlan(virtual_network, vmware.nsx_edge_v_tep_vlan_id),
                        'nsx_edge_uplink1_vlan_id': str(vmware.nsx_edge_uplink1_vlan_id),
                        'nsx_edge_uplink1_vlan': self.__load_core_network_single_vlan(virtual_network, vmware.nsx_edge_uplink1_vlan_id),
                        'nsx_edge_uplink2_vlan_id': str(vmware.nsx_edge_uplink2_vlan_id),
                        'nsx_edge_uplink2_vlan': self.__load_core_network_single_vlan(virtual_network, vmware.nsx_edge_uplink2_vlan_id),
                        'hcx_private_ip_id': str(vmware.hcx_private_ip_id),
                        'hcx_fqdn': str(vmware.hcx_fqdn),
                        'hcx_initial_password': str(vmware.hcx_initial_password),
                        'hcx_vlan_id': str(vmware.hcx_vlan_id),
                        'hcx_on_prem_key': str(vmware.hcx_on_prem_key),
                        'is_hcx_enabled': str(vmware.is_hcx_enabled),
                        'time_created': str(vmware.time_created),
                        'time_updated': str(vmware.time_updated),
                        'lifecycle_state': str(vmware.lifecycle_state),
                        'sum_info': "PaaS OCVS VMWare ESXi Servers",
                        'sum_size_gb': str(vmware.esxi_hosts_count),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'defined_tags': [] if vmware.defined_tags is None else vmware.defined_tags,
                        'freeform_tags': [] if vmware.freeform_tags is None else vmware.freeform_tags,
                        'esxihosts': [],
                        'region_name': str(self.config['region'])}

                    #######################
                    # get the esxi hosts
                    #######################
                    esxis = []
                    try:
                        esxis = esxi_client.list_esxi_hosts(
                            sddc_id=vmware.id,
                            sort_by="displayName",
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                    except oci.exceptions.ServiceError:
                        pass
                    except oci.exceptions.ConnectTimeout:
                        pass

                    # esxi = classoci.ocvp.models.EsxiHostSummary
                    if esxis:
                        for esxi in esxis.items:
                            if self.check_lifecycle_state_active(esxi.lifecycle_state):
                                val['esxihosts'].append(
                                    {
                                        'id': str(esxi.id),
                                        'display_name': str(esxi.display_name),
                                        'compute_instance_id': str(esxi.compute_instance_id),
                                        'billing_contract_end_date': str(esxi.billing_contract_end_date),
                                        'current_sku': str(esxi.current_sku),
                                        'next_sku': str(esxi.next_sku),
                                        'time_created': str(esxi.time_created),
                                        'time_updated': str(esxi.time_updated),
                                        'lifecycle_state': str(esxi.lifecycle_state),
                                        'defined_tags': [] if esxi.defined_tags is None else esxi.defined_tags,
                                        'freeform_tags': [] if esxi.freeform_tags is None else esxi.freeform_tags
                                    }
                                )

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_paas_ocvs", e, compartment)
            return data

    ##########################################################################
    # __load_paas_oac
    ##########################################################################
    def __load_paas_oac(self, oac_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "OAC Native"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                oacs = []
                try:
                    oacs = oci.pagination.list_call_get_all_results(
                        oac_client.list_analytics_instances,
                        compartment['id'],
                        sort_by="name",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    # for OAC skip this region
                    break

                if self.flags.skip_threads:
                    print(".", end="")

                # oac = oci.analytics.models.AnalyticsInstanceSummary
                for oac in oacs:
                    if (oac.lifecycle_state != 'DELETED'):

                        val = {'id': str(oac.id),
                               'name': str(oac.name),
                               'description': str(oac.description),
                               'time_created': str(oac.time_created),
                               'time_updated': str(oac.time_updated),
                               'lifecycle_state': str(oac.lifecycle_state),
                               'feature_set': str(oac.feature_set),
                               'license_type': str(oac.license_type),
                               'capacity_type': str(oac.capacity.capacity_type),
                               'capacity_value': str(oac.capacity.capacity_value),
                               'email_notification': str(oac.email_notification),
                               'service_url': str(oac.service_url),
                               'vanity_domain': "",
                               'vanity_url': "",
                               'sum_info': "PaaS OAC Native " + str(oac.capacity.capacity_type) + " " + ("BYOL" if 'BRING' in oac.license_type else "INCL"),
                               'sum_size_gb': str(oac.capacity.capacity_value),
                               'network_endpoint_details': str(oac.network_endpoint_details.network_endpoint_type),
                               'defined_tags': [],
                               'freeform_tags': [],
                               'compartment_name': str(compartment['name']),
                               'compartment_path': str(compartment['path']),
                               'compartment_id': str(compartment['id']),
                               'region_name': str(self.config['region'])}

                        # Fetch main OAC object for Vanity URL
                        try:
                            oac_main = oac_client.get_analytics_instance(oac.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                            val['defined_tags'] = [] if oac_main.defined_tags is None else oac_main.defined_tags
                            val['freeform_tags'] = [] if oac_main.freeform_tags is None else oac_main.freeform_tags
                            if oac_main.vanity_url_details:
                                for k, v in oac_main.vanity_url_details.items():
                                    if v:
                                        val['vanity_domain'] = str(', '.join(x for x in v.hosts))
                                        val['vanity_url'] = str(', '.join(x for x in v.urls))

                        except oci.exceptions.ServiceError:
                            pass

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_paas_oac", e, compartment)
            return data

    ##########################################################################
    # __load_paas_oce
    ##########################################################################
    def __load_paas_oce(self, oce_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "OCE Native"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                oces = []
                try:
                    oces = oci.pagination.list_call_get_all_results(
                        oce_client.list_oce_instances,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # oce = oci.oce.models.OceInstanceSummary
                for oce in oces:
                    if not self.check_lifecycle_state_active(oce.lifecycle_state):
                        continue

                    val = {
                        'id': str(oce.id),
                        'guid': str(oce.guid),
                        'description': str(oce.description),
                        'name': str(oce.name),
                        'tenancy_name': str(oce.tenancy_name),
                        'idcs_tenancy': str(oce.idcs_tenancy),
                        'object_storage_namespace': str(oce.object_storage_namespace),
                        'admin_email': str(oce.admin_email),
                        'time_created': str(oce.time_created),
                        'time_updated': str(oce.time_updated),
                        'lifecycle_state': str(oce.lifecycle_state),
                        'state_message': str(oce.state_message),
                        'service': oce.service,
                        'sum_info': "PaaS OCE Native",
                        'sum_size_gb': str("1"),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'defined_tags': [] if oce.defined_tags is None else oce.defined_tags,
                        'freeform_tags': [] if oce.freeform_tags is None else oce.freeform_tags,
                        'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_paas_oce", e, compartment)
            return data

    ##########################################################################
    # __load_paas_visualbuilder
    ##########################################################################
    def __load_paas_visualbuilder(self, vb_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Visual Builder"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                vbs = []
                try:
                    vbs = oci.pagination.list_call_get_all_results(
                        vb_client.list_vb_instances,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # vbs = oci.visual_builder.models.VbInstanceSummary
                for vb in vbs:
                    if self.check_lifecycle_state_active(vb.lifecycle_state):
                        val = {'id': str(vb.id),
                               'display_name': str(vb.display_name),
                               'time_created': str(vb.time_created),
                               'time_updated': str(vb.time_updated),
                               'lifecycle_state': str(vb.lifecycle_state),
                               'state_message': str(vb.state_message),
                               'instance_url': str(vb.instance_url),
                               'node_count': str(vb.node_count),
                               'is_visual_builder_enabled': str(vb.is_visual_builder_enabled),
                               'custom_endpoint': str(vb.custom_endpoint.hostname) if vb.custom_endpoint else "",
                               'alternate_custom_endpoints': str(vb.alternate_custom_endpoints.hostname) if vb.alternate_custom_endpoints else "",
                               'consumption_model': str(vb.consumption_model),
                               'sum_info': "PaaS Visual Builder",
                               'sum_size_gb': str(vb.node_count),
                               'compartment_name': str(compartment['name']),
                               'compartment_path': str(compartment['path']),
                               'compartment_id': str(compartment['id']),
                               'defined_tags': [] if vb.defined_tags is None else vb.defined_tags,
                               'system_tags': [] if vb.system_tags is None else vb.system_tags,
                               'freeform_tags': [] if vb.freeform_tags is None else vb.freeform_tags,
                               'region_name': str(self.config['region'])}

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_paas_visualbuilder", e, compartment)
            return data

    ##########################################################################
    # __load_paas_open_search
    ##########################################################################
    def __load_paas_open_search(self, open_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Open Search Cluster"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                opens = []
                try:
                    opens = oci.pagination.list_call_get_all_results(
                        open_client.list_opensearch_clusters,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.opensearch.models.OpensearchClusterSummary
                for arr in opens:
                    if not self.check_lifecycle_state_active(arr.lifecycle_state):
                        continue

                    val = {
                        'id': str(arr.id),
                        'display_name': str(arr.display_name),
                        'time_created': str(arr.time_created),
                        'time_updated': str(arr.time_updated),
                        'lifecycle_state': str(arr.lifecycle_state),
                        'software_version': str(arr.software_version),
                        'total_storage_gb': str(arr.total_storage_gb),
                        'security_mode': str(arr.security_mode) if arr.security_mode else "",
                        'availability_domains': str(", ").join(x for x in arr.availability_domains) if arr.availability_domains else "",
                        'sum_info': "PaaS Open Search Cluster",
                        'sum_size_gb': str(1),
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                        'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        'region_name': str(self.config['region'])
                    }

                    val['opensearch_fqdn'] = ""
                    val['opensearch_private_ip'] = ""
                    val['opendashboard_fqdn'] = ""
                    val['opendashboard_private_ip'] = ""
                    val['master_node_count'] = ""
                    val['master_node_host_type'] = ""
                    val['master_node_host_bare_metal_shape'] = ""
                    val['master_node_host_ocpu_count'] = ""
                    val['master_node_host_memory_gb'] = ""
                    val['data_node_count'] = ""
                    val['data_node_host_type'] = ""
                    val['data_node_host_bare_metal_shape'] = ""
                    val['data_node_host_ocpu_count'] = ""
                    val['data_node_host_memory_gb'] = ""
                    val['data_node_storage_gb'] = ""
                    val['opendashboard_node_count'] = ""
                    val['opendashboard_node_host_ocpu_count'] = ""
                    val['opendashboard_node_host_memory_gb'] = ""
                    val['vcn_id'] = ""
                    val['vcn_name'] = ""
                    val['subnet_id'] = ""
                    val['subnet_name'] = ""
                    val['vcn_compartment_id'] = ""
                    val['subnet_compartment_id'] = ""
                    val['security_master_user_name'] = ""
                    val['security_master_user_password_hash'] = ""

                    try:
                        # get the target with more info
                        arf = open_client.get_opensearch_cluster(
                            arr.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                        # target_detector_recipes
                        val['opensearch_fqdn'] = str(arf.opensearch_fqdn)
                        val['opensearch_private_ip'] = str(arf.opensearch_private_ip)
                        val['opendashboard_fqdn'] = str(arf.opendashboard_fqdn)
                        val['opendashboard_private_ip'] = str(arf.opendashboard_private_ip)
                        val['master_node_count'] = str(arf.master_node_count)
                        val['master_node_host_type'] = str(arf.master_node_host_type)
                        val['master_node_host_bare_metal_shape'] = str(arf.master_node_host_bare_metal_shape)
                        val['master_node_host_ocpu_count'] = str(arf.master_node_host_ocpu_count)
                        val['master_node_host_memory_gb'] = str(arf.master_node_host_memory_gb)
                        val['data_node_count'] = str(arf.data_node_count)
                        val['data_node_host_type'] = str(arf.data_node_host_type)
                        val['data_node_host_bare_metal_shape'] = str(arf.data_node_host_bare_metal_shape)
                        val['data_node_host_ocpu_count'] = str(arf.data_node_host_ocpu_count)
                        val['data_node_host_memory_gb'] = str(arf.data_node_host_memory_gb)
                        val['data_node_storage_gb'] = str(arf.data_node_storage_gb)
                        val['opendashboard_node_count'] = str(arf.opendashboard_node_count)
                        val['opendashboard_node_host_ocpu_count'] = str(arf.opendashboard_node_host_ocpu_count)
                        val['opendashboard_node_host_memory_gb'] = str(arf.opendashboard_node_host_memory_gb)
                        val['vcn_id'] = str(arf.vcn_id)
                        val['vcn_name'] = self.get_network_vcn(arf.vcn_id)
                        val['subnet_id'] = self.get_network_subnet(arf.subnet_id, detailed=True)
                        val['vcn_compartment_id'] = str(arf.vcn_compartment_id)
                        val['subnet_compartment_id'] = str(arf.subnet_compartment_id)
                        val['security_master_user_name'] = str(arf.security_master_user_name)
                        val['security_master_user_password_hash'] = str(arf.security_master_user_password_hash)

                    except Exception as e:
                        self.__print_error("__load_paas_open_search", e)

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_paas_open_search", e, compartment)
            return data

    ##########################################################################
    # __load_paas_devops
    ##########################################################################
    def __load_paas_devops(self, devops_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "DevOps Project"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        devops_client.list_projects,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # arr = oci.devops.models.ProjectSummary
                for arr in array:
                    if self.check_lifecycle_state_active(arr.lifecycle_state):
                        val = {'id': str(arr.id),
                               'name': str(arr.name),
                               'description': str(arr.description),
                               'namespace': str(arr.namespace),
                               'time_created': str(arr.time_created),
                               'time_updated': str(arr.time_updated),
                               'lifecycle_state': str(arr.lifecycle_state),
                               'notification_config': "",
                               'sum_info': "DevOPS Projects",
                               'sum_size_gb': str("1"),
                               'compartment_name': str(compartment['name']),
                               'compartment_path': str(compartment['path']),
                               'compartment_id': str(compartment['id']),
                               'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                               'system_tags': [] if arr.system_tags is None else arr.system_tags,
                               'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                               'region_name': str(self.config['region'])}

                        # notification_config
                        if arr.notification_config:
                            val['notification_config'] = str(arr.notification_config.topic_id)

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_paas_devops", e)
            return data

    ##########################################################################
    # __load_limits
    ##########################################################################
    def __load_limits(self, limits_client, tenancy_id, compartments):
        data = []
        cnt = 0
        start_time = time.time()

        if self.EXCLUDE_LIMITS in self.flags.exclude:
            return data

        try:
            errstr = ""
            header = "Limits"
            self.__load_print_status_with_threads(header)

            services = []
            try:
                services = oci.pagination.list_call_get_all_results(
                    limits_client.list_services,
                    tenancy_id, sort_by="name",
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data
            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning("a", False)
                else:
                    raise

            if services:

                # oci.limits.models.ServiceSummary
                for service in services:
                    if self.flags.skip_threads:
                        print(".", end="")

                    # get the limits per service
                    limits = []
                    try:
                        limits = oci.pagination.list_call_get_all_results(
                            limits_client.list_limit_values,
                            tenancy_id,
                            service_name=service.name,
                            sort_by="name",
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data
                    except oci.exceptions.Exception as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning("a", False, to_print=self.flags.skip_threads)
                            errstr += "a"
                        else:
                            raise

                    # oci.limits.models.LimitValueSummary
                    for limit in limits:
                        val = {
                            'name': str(service.name),
                            'description': str(service.description),
                            'limit_name': str(limit.name),
                            'availability_domain': ("" if limit.availability_domain is None else str(limit.availability_domain)),
                            'scope_type': str(limit.scope_type),
                            'value': str(limit.value),
                            'used': "",
                            'available': "",
                            'region_name': str(self.config['region'])
                        }

                        # if not limit, continue, don't calculate limit = 0
                        if limit.value == 0:
                            continue

                        # get usage per limit if available
                        try:
                            limit_compartment = tenancy_id

                            # if only one compartment filtered check the compartment limit
                            if len(compartments) == 1:
                                limit_compartment = compartments[0]['id']

                            usage = []
                            if limit.scope_type == "AD":
                                usage = limits_client.get_resource_availability(service.name, limit.name, limit_compartment, availability_domain=limit.availability_domain).data
                            else:
                                usage = limits_client.get_resource_availability(service.name, limit.name, limit_compartment).data

                            # oci.limits.models.ResourceAvailability
                            if usage.used is not None:
                                val['used'] = str(usage.used)
                            if usage.available is not None:
                                val['available'] = str(usage.available)
                        except oci.exceptions.ServiceError as e:
                            if e.code == 'NotAuthorizedOrNotFound':
                                val['used'] = 'NotAuth'
                                val['available'] = 'NotAuth'
                        except Exception:
                            pass

                        # add to array
                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_limits", e)
            return data

    ##########################################################################
    # __load_quotas
    ##########################################################################
    def __load_quotas(self, quotas_client, compartments):
        data = []
        cnt = 0
        start_time = time.time()

        try:
            if self.EXCLUDE_QUOTAS in self.flags.exclude:
                return data

            errstr = ""
            header = "Quotas"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip Paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                # skip if not root compartment
                if compartment['id'] != self.get_tenancy_id():
                    continue

                quotas = []
                try:
                    quotas = quotas_client.list_quotas(
                        compartment['id'],
                        lifecycle_state=oci.limits.models.QuotaSummary.LIFECYCLE_STATE_ACTIVE,
                        sort_by="NAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data
                except oci.exceptions.ServiceError as e:
                    if 'go to your home region' in str(e):
                        errstr = "Can run on home region only, skipping."
                        self.__load_print_thread_cnt(header, cnt, start_time, errstr)
                        return data
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                    else:
                        raise

                if self.flags.skip_threads:
                    print(".", end="")

                if quotas:

                    # oci.limits.models.QuotaSummary
                    for arr in quotas:

                        val = {
                            'id': str(arr.id),
                            'name': str(arr.name),
                            'description': str(arr.description),
                            'statements': [],
                            'time_created': str(arr.time_created),
                            'compartment_name': str(compartment['name']),
                            'compartment_path': str(compartment['path']),
                            'compartment_id': str(compartment['id']),
                            'region_name': str(self.config['region']),
                            'defined_tags': [] if arr.defined_tags is None else arr.defined_tags,
                            'freeform_tags': [] if arr.freeform_tags is None else arr.freeform_tags,
                        }

                        # read quota statements
                        try:
                            quota = quotas_client.get_quota(arr.id).data
                            if quota:
                                val['statements'] = quota.statements
                        except oci.exceptions.ServiceError:
                            pass

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_quotas", e)
            return data

    ##########################################################################
    # __load_security_cloud_guard
    ##########################################################################
    def __load_security_cloud_guard(self, cg_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Cloud Guard"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        cg_client.list_targets,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # item = oci.cloud_guard.models.TargetSummary
                for item in array:
                    if not self.check_lifecycle_state_active(item.lifecycle_state):
                        continue

                    val = {
                        'id': str(item.id),
                        'display_name': str(item.display_name),
                        'target_resource_type': str(item.target_resource_type),
                        'target_resource_id': str(item.target_resource_id),
                        'target_resource_name': "",
                        'inherited_by_compartments': "",
                        'inherited_by_compartments_names': "",
                        'target_detector_recipes': [],
                        'target_responder_recipes': [],
                        'recipe_count': str(item.recipe_count),
                        'time_created': str(item.time_created),
                        'time_updated': str(item.time_updated),
                        'lifecycle_state': str(item.lifecycle_state),
                        'lifecyle_details': str(item.lifecyle_details),
                        'sum_info': "Cloud Guard",
                        'sum_size_gb': str(1),
                        'system_tags': [] if item.system_tags is None else item.system_tags,
                        'defined_tags': [] if item.defined_tags is None else item.defined_tags,
                        'freeform_tags': [] if item.freeform_tags is None else item.freeform_tags,
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])}

                    # target compartment name
                    target_arr = self.get_compartment_by_id(item.target_resource_id)
                    if target_arr:
                        val['target_resource_name'] = target_arr['name']

                    try:
                        # get the target with more info
                        itemfull = cg_client.get_target(
                            item.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                        if itemfull.inherited_by_compartments:
                            incp = []
                            for cp in itemfull.inherited_by_compartments:
                                cpname = self.get_compartment_by_id(cp)
                                if cpname:
                                    incp.append(cpname['name'])
                            val['inherited_by_compartments'] = str(','.join(y for y in itemfull.inherited_by_compartments))
                            val['inherited_by_compartments_names'] = str(','.join(y for y in incp))

                        # target_detector_recipes
                        val['target_detector_recipes'] = [{
                            'id': str(arr.id),
                            'display_name': str(arr.display_name),
                            'description': str(arr.description),
                            'compartment_id': str(arr.compartment_id),
                            'detector_recipe_id': str(arr.detector_recipe_id),
                            'owner': str(arr.owner),
                            'detector': str(arr.detector),
                            'effective_detector_rules': [y.detector_rule_id for y in arr.effective_detector_rules] if arr.effective_detector_rules else [],
                            'time_created': str(arr.time_created),
                            'time_updated': str(arr.time_updated),
                            'lifecycle_state': str(arr.lifecycle_state),
                            'source_data_retention': str(arr.source_data_retention)
                        } for arr in itemfull.target_detector_recipes] if itemfull.target_detector_recipes else []

                        # target_responder_recipes
                        val['target_responder_recipes'] = [{
                            'id': str(arr.id),
                            'responder_recipe_id': str(arr.responder_recipe_id),
                            'compartment_id': str(arr.compartment_id),
                            'display_name': str(arr.display_name),
                            'description': str(arr.description),
                            'owner': str(arr.owner),
                            'time_created': str(arr.time_created),
                            'time_updated': str(arr.time_updated),
                            'effective_responder_rules': [y.responder_rule_id for y in arr.effective_responder_rules] if arr.effective_responder_rules else [],
                        } for arr in itemfull.target_responder_recipes] if itemfull.target_responder_recipes else []
                    except Exception as e:
                        self.__print_error("__load_security_cloud_guard", e)

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_security_cloud_guard", e)
            return data

    ##########################################################################
    # __load_security_scores_main
    ##########################################################################
    #
    # OCI Classes used:
    #
    # oci.cloud_guard.CloudGuardClient(config, **kwargs)
    ##########################################################################
    def __load_security_scores_main(self):

        try:
            print("Cloud Guard Scores...")

            # clients
            cg_client = oci.cloud_guard.CloudGuardClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))

            if self.flags.proxy:
                cg_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to compartments
            root_compartment = self.get_tenancy_id()

            # add the key if not exists
            self.__initialize_data_key(self.C_SECURITY_SCORES, self.C_SECURITY_SCORES_GUARD_SECURITY_SCORES)
            self.__initialize_data_key(self.C_SECURITY_SCORES, self.C_SECURITY_SCORES_GUARD_RISK_SCORES)

            # reference to paas
            sec = self.data[self.C_SECURITY_SCORES]

            # append the data
            sec[self.C_SECURITY_SCORES_GUARD_SECURITY_SCORES] += self.__load_security_cloud_guard_security_scores(cg_client, root_compartment)
            sec[self.C_SECURITY_SCORES_GUARD_RISK_SCORES] += self.__load_security_cloud_guard_risk_scores(cg_client, root_compartment)

            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_security_scores_main", e)

    ##########################################################################
    # __load_security_kms_vaults
    ##########################################################################
    def __load_security_kms_vaults(self, kms_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Key Vaults"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        kms_client.list_vaults,
                        compartment['id'],
                        sort_by="DISPLAYNAME",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # item = oci.key_management.models.VaultSummary
                for item in array:
                    if self.check_lifecycle_state_active(item.lifecycle_state):

                        val = {'id': str(item.id),
                               'name': str(item.display_name),
                               'crypto_endpoint': str(item.crypto_endpoint),
                               'management_endpoint': str(item.management_endpoint),
                               'vault_type': str(item.vault_type),
                               'time_created': str(item.time_created),
                               'lifecycle_state': str(item.lifecycle_state),
                               'sum_info': "KMS Vaults",
                               'sum_info_hsm': "KMS HSM Keys",
                               'sum_info_soft': "KMS Soft Keys",
                               'sum_size_gb': str(1),
                               'defined_tags': [] if item.defined_tags is None else item.defined_tags,
                               'freeform_tags': [] if item.freeform_tags is None else item.freeform_tags,
                               'compartment_name': str(compartment['name']),
                               'compartment_path': str(compartment['path']),
                               'key_count': "0",
                               'key_version_count': "0",
                               'software_key_count': "0",
                               'software_key_version_count': "0",
                               'replicas': [],
                               'compartment_id': str(compartment['id']),
                               'region_name': str(self.config['region'])}

                        # get vault usage
                        # oci.key_management.models.VaultUsage
                        try:
                            usage = kms_client.get_vault_usage(item.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                            val['key_count'] = str(usage.key_count)
                            val['key_version_count'] = str(usage.key_version_count)
                            val['software_key_count'] = str(usage.software_key_count)
                            val['software_key_version_count'] = str(usage.software_key_version_count)

                        except Exception:
                            pass

                        # get vault replicas
                        # oci.key_management.models.VaultReplicaSummary
                        try:
                            replicas = kms_client.list_vault_replicas(item.id, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY).data
                            repval = []
                            for rep in replicas:
                                repval.append({
                                    'crypto_endpoint': str(rep.crypto_endpoint),
                                    'management_endpoint': str(rep.management_endpoint),
                                    'region': str(rep.region),
                                    'status': str(rep.status)
                                })
                            val['replicas'] = repval

                        except Exception:
                            pass

                        # add the data
                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_security_kms_vaults", e)
            return data

    ##########################################################################
    # __load_security_cloud_guard_risk_scores
    ##########################################################################
    def __load_security_cloud_guard_risk_scores(self, cg_client, root_compartment):

        data = []
        start_time = time.time()

        try:
            errstr = ""
            header = "Risk Scores"
            self.__load_print_status_with_threads(header)

            array = []
            try:
                array = cg_client.request_risk_scores(
                    root_compartment,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

            except oci.exceptions.ServiceError as e:
                if e.code == 404:
                    print(" Not Enabled")
                    return data
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning()
                    return data
                raise
            except oci.exceptions.ConnectTimeout:
                self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                errstr += "a"
                return data

            # item = oci.cloud_guard.models.TargetSummary
            for item in array.items:
                val = {'dimensions_map': item.dimensions_map,
                       'risk_score': item.risk_score}

                data.append(val)

            cnt = 1
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_security_cloud_guard_risk_scores", e)
            return data

    ##########################################################################
    # __load_security_cloud_guard_risk_scores
    ##########################################################################
    def __load_security_cloud_guard_security_scores(self, cg_client, root_compartment):

        data = []
        start_time = time.time()

        try:
            errstr = ""
            header = "Security Scores"
            self.__load_print_status_with_threads(header)

            array = []
            try:
                array = cg_client.request_security_scores(
                    root_compartment,
                    retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                ).data

            except oci.exceptions.ServiceError as e:
                if e.code == 404:
                    print(" Not Enabled")
                    return data
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    return data
                raise
            except oci.exceptions.ConnectTimeout:
                self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                errstr += "a"
                return data

            for item in array.items:
                val = {'dimensions_map': item.dimensions_map,
                       'security_rating': str(item.security_rating),
                       'security_score': item.security_score}

                data.append(val)

            cnt = 1
            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_security_cloud_guard_security_scores", e)
            return data

    ##########################################################################
    # __load_security_log_groups
    ##########################################################################
    def __load_security_log_groups(self, log_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Logging Groups"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        log_client.list_log_groups,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # item = oci.logging.models.LogGroupSummary
                for item in array:
                    val = {
                        'id': str(item.id),
                        'display_name': str(item.display_name),
                        'description': str(item.description),
                        'time_created': str(item.time_created),
                        'time_last_modified': str(item.time_last_modified),
                        'sum_info': "Log Groups",
                        'sum_size_gb': str(1),
                        'logs': [],
                        'defined_tags': [] if item.defined_tags is None else item.defined_tags,
                        'freeform_tags': [] if item.freeform_tags is None else item.freeform_tags,
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])
                    }

                    ######################
                    # obtain logs info
                    ######################
                    logs = []
                    try:
                        logs = oci.pagination.list_call_get_all_results(
                            log_client.list_logs,
                            item.id,
                            sort_by="displayName",
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                    except oci.exceptions.ServiceError as e:
                        if self.__check_service_error(e.code):
                            self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                            errstr += "a"
                            continue
                        raise
                    except oci.exceptions.ConnectTimeout:
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue

                    # log_item = oci.logging.models.LogSummary
                    for log_item in logs:
                        enabled_str = "Enabled" if log_item.is_enabled else "Not Enabled"
                        log_val = {
                            'log_group_id': str(item.id),
                            'log_group_name': str(item.display_name),
                            'id': str(log_item.id),
                            'display_name': str(log_item.display_name),
                            'is_enabled': str(log_item.is_enabled),
                            'name': str(item.display_name) + " - " + str(log_item.display_name) + " - " + enabled_str,
                            'archiving': "",
                            'source_service': "",
                            'source_category': "",
                            'source_sourcetype': "",
                            'source_resource': "",
                            'source_parameters': {},
                            'lifecycle_state': str(log_item.lifecycle_state),
                            'log_type': str(log_item.log_type),
                            'defined_tags': [] if item.defined_tags is None else item.defined_tags,
                            'freeform_tags': [] if item.freeform_tags is None else item.freeform_tags,
                            'time_created': str(log_item.time_created),
                            'retention_duration': str(log_item.retention_duration),
                            'time_last_modified': str(log_item.time_last_modified),
                            'compartment_name': str(compartment['name']),
                            'compartment_path': str(compartment['path']),
                            'compartment_id': str(compartment['id']),
                            'region_name': str(self.config['region'])
                        }

                        # source and archive configuration
                        try:
                            # oci.logging.models.Archiving
                            archiving = log_item.configuration.archiving
                            log_val['archiving'] = str(archiving.is_enabled)

                            # oci.logging.models.Source
                            source = log_item.configuration.source
                            log_val['source_sourcetype'] = str(source.source_type)

                            # oci.logging.models.OciService
                            if source.source_type == 'OCISERVICE':
                                log_val['source_service'] = str(source.service)
                                log_val['source_category'] = str(source.category)
                                log_val['source_resource'] = str(source.resource)
                                log_val['source_parameters'] = source.parameters

                        except Exception:
                            continue

                        val["logs"].append(log_val)

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_security_log_groups", e, compartment)
            return data

    ##########################################################################
    # __load_security_log_unified_agents
    ##########################################################################
    def __load_security_log_unified_agents(self, log_client, compartments):

        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Logging Unified Agenets"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                array = []
                try:
                    array = oci.pagination.list_call_get_all_results(
                        log_client.list_unified_agent_configurations,
                        compartment['id'],
                        sort_by="displayName",
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    continue

                if self.flags.skip_threads:
                    print(".", end="")

                # item = oci.logging.models.UnifiedAgentConfigurationSummary
                for item in array:
                    val = {
                        'id': str(item.id),
                        'display_name': self.get_value(item.display_name),
                        'description': self.get_value(item.description),
                        'time_created': self.get_value(item.time_created),
                        'time_last_modified': self.get_value(item.time_last_modified),
                        'is_enabled': self.get_value(item.is_enabled),
                        'configuration_type': self.get_value(item.configuration_type),
                        'configuration_state': self.get_value(item.configuration_state),
                        'sum_info': "Log Unified Agents",
                        'sum_size_gb': str(1),
                        'defined_tags': [] if item.defined_tags is None else item.defined_tags,
                        'freeform_tags': [] if item.freeform_tags is None else item.freeform_tags,
                        'service_configuration_source': [],
                        'service_configuration_dest': '',
                        'group_association': [],
                        'compartment_name': str(compartment['name']),
                        'compartment_path': str(compartment['path']),
                        'compartment_id': str(compartment['id']),
                        'region_name': str(self.config['region'])
                    }

                    # item2 = oci.logging.models.UnifiedAgentConfiguration
                    try:
                        item2 = log_client.get_unified_agent_configuration(
                            item.id,
                            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                        ).data

                        # service_configuration
                        if item2.service_configuration.configuration_type:
                            if item2.service_configuration.configuration_type == 'LOGGING':
                                for src in item2.service_configuration.sources:
                                    if src.source_type == "LOG_TAIL":
                                        val['service_configuration_source'].append({
                                            'name': src.name,
                                            'source_type': src.source_type,
                                            'paths': src.paths,
                                            'parser_type': src.parser.parser_type if src.parser else ""})
                                    elif src.source_type == "WINDOWS_EVENT_LOG":
                                        val['service_configuration_source'].append({
                                            'name': src.name,
                                            'source_type': src.source_type,
                                            'channels': src.channels})
                                    else:
                                        val['service_configuration_source'].append({'name': src.name, 'source_type': src.source_type})

                                if item2.service_configuration.destination:
                                    val['service_configuration_dest'] = item2.service_configuration.destination.log_object_id

                        # group_association
                        if item2.group_association:
                            val['service_configuration_dest'] = item2.group_association.group_list

                    except oci.exceptions.ServiceError:
                        errstr += "a"
                    except oci.exceptions.ConnectTimeout:
                        errstr += "a"

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_security_log_unified_agents", e, compartment)
            return data

    ##########################################################################
    # __load_security_bastions
    ##########################################################################
    def __load_security_bastions(self, bs_client, compartments):
        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Bastions"
            self.__load_print_status_with_threads(header)

            # loop on all compartments
            for compartment in compartments:

                # skip managed paas compartment
                if self.__if_managed_paas_compartment(compartment['name']):
                    continue

                bastions = []
                try:
                    bastions = oci.pagination.list_call_get_all_results(
                        bs_client.list_bastions,
                        compartment['id'],
                        retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
                    ).data

                except oci.exceptions.ServiceError as e:
                    if self.__check_service_error(e.code):
                        self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                        errstr += "a"
                        continue
                    raise
                except oci.exceptions.ConnectTimeout:
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                    break

                if self.flags.skip_threads:
                    print(".", end="")

                # bs = oci.bastion.models.BastionSummary
                for bs in bastions:
                    if self.check_lifecycle_state_active(bs.lifecycle_state):
                        val = {
                            'id': str(bs.id),
                            'bastion_type': str(bs.bastion_type),
                            'name': str(bs.name),
                            'target_vcn_id': str(bs.target_vcn_id),
                            'target_vcn_name': self.get_network_vcn(bs.target_vcn_id),
                            'target_subnet_id': str(bs.target_subnet_id),
                            'target_subnet_name': self.get_network_subnet(bs.target_subnet_id),
                            'time_created': str(bs.time_created),
                            'time_updated': str(bs.time_updated),
                            'lifecycle_state': str(bs.lifecycle_state),
                            'defined_tags': [] if bs.defined_tags is None else bs.defined_tags,
                            'freeform_tags': [] if bs.freeform_tags is None else bs.freeform_tags,
                            'lifecycle_details': str(bs.lifecycle_details),
                            'sum_info': "Bastions",
                            'sum_size_gb': str(1),
                            'compartment_name': str(compartment['name']),
                            'compartment_path': str(compartment['path']),
                            'compartment_id': str(compartment['id']),
                            'region_name': str(self.config['region'])
                        }

                        cnt += 1
                        data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return data
            raise
        except Exception as e:
            self.__print_error("__load_security_bastions", e, compartment)
            return data

    ##########################################################################
    # __load_announcement_main
    ##########################################################################
    def __load_announcement_main(self):
        try:
            print("Announcements...")

            # AnnouncementClient
            announcement_client = oci.announcements_service.AnnouncementClient(self.config, signer=self.signer, timeout=(self.flags.connection_timeout, self.flags.read_timeout))
            if self.flags.proxy:
                announcement_client.base_client.session.proxies = {'https': self.flags.proxy}

            # reference to tenancy
            tenancy = self.get_tenancy()

            # add the key if not exists
            self.__initialize_data_key(self.C_ANNOUNCEMENT, self.C_ANNOUNCEMENT_ANNOUNCEMENT)

            # reference to stream
            announcement = self.data[self.C_ANNOUNCEMENT]

            # append the data
            announcement[self.C_ANNOUNCEMENT_ANNOUNCEMENT] += self.__load_announcements(announcement_client, tenancy['id'])
            print("")

        except oci.exceptions.RequestException:
            raise
        except oci.exceptions.ServiceError:
            raise
        except Exception as e:
            self.__print_error("__load_announcement_main", e)

    ##########################################################################
    # __load_announcements
    ##########################################################################
    def __load_announcements(self, announcement_client, tenancy_id):
        data = []
        cnt = 0
        start_time = time.time()

        try:
            errstr = ""
            header = "Announcement Items"
            self.__load_print_status_with_threads(header)

            announcements = []
            try:
                announcements = oci.pagination.list_call_get_all_results(
                    announcement_client.list_announcements,
                    tenancy_id,
                    sort_by="timeCreated"
                ).data

            except oci.exceptions.ServiceError as e:
                if self.__check_service_error(e.code):
                    self.__load_print_auth_warning(to_print=self.flags.skip_threads)
                    errstr += "a"
                else:
                    raise

            if self.flags.skip_threads:
                print(".", end="")

            if announcements:

                # oci.announcements_service.models.AnnouncementsCollection
                # oci.announcements_service.models.AnnouncementSummary
                for ann in announcements:
                    val = {'id': str(ann.id),
                           'type': str(ann.type),
                           'lifecycle_state': str(ann.lifecycle_state),
                           'reference_ticket_number': str(ann.reference_ticket_number),
                           'summary': str(ann.summary),
                           'time_one_title': str(ann.time_one_title),
                           'time_one_value': str(ann.time_one_value),
                           'time_two_title': str(ann.time_two_title),
                           'time_two_value': str(ann.time_two_value),
                           'services': str(ann.services),
                           'affected_regions': str(', '.join(x for x in ann.affected_regions)),
                           'announcement_type': str(ann.announcement_type),
                           'is_banner': ann.is_banner,
                           'time_created': str(ann.time_created),
                           'time_updated': str(ann.time_updated),
                           'region_name': str(self.config['region'])}

                    # add the data
                    cnt += 1
                    data.append(val)

            self.__load_print_thread_cnt(header, cnt, start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:

            if self.__check_request_error(e):
                return data

            raise
        except Exception as e:
            self.__print_error("__load_announcements", e)
            return data


##########################################################################
# class ShowOCIFlags
##########################################################################
class ShowOCIFlags(object):
    # Read Flags
    read_identity = False
    read_identity_compartments = False
    read_network = False
    read_compute = False
    read_database = False
    read_file_storage = False
    read_object_storage = False
    read_load_balancer = False
    read_email_distribution = False
    read_resource_management = False
    read_containers = False
    read_streams_queues = False
    read_budgets = False
    read_monitoring_notifications = False
    read_edge = False
    read_announcement = False
    read_ManagedCompartmentForPaaS = True
    read_root_compartment = True
    read_paas_native = False
    read_security = False
    read_function = False
    read_api = False
    read_limits = False
    read_data_ai = False
    skip_identity_user_credential = False
    skip_backups = False
    skip_threads = False
    threads = 8
    skip_dbhomes = False
    exclude = []
    connection_timeout = 20
    read_timeout = 150

    # is_vcn_exist_for_region
    is_vcn_exist_for_region = False

    # filter flags
    filter_by_region = ""
    filter_by_region_not = ""
    filter_by_compartment = ""
    filter_by_compartment_recursive = ""
    filter_by_compartment_path = ""
    filter_by_tenancy_id = ""

    # version, config files and proxy
    proxy = ""
    showoci_version = ""
    config_file = oci.config.DEFAULT_LOCATION
    config_section = oci.config.DEFAULT_PROFILE
    use_instance_principals = False
    use_resource_principals = False
    use_delegation_token = False
    use_security_token = False

    # pyton and host info
    machine = platform.node() + " (" + platform.machine() + ")"
    python = platform.python_version()

    # flag if to run on compartment
    run_on_compartments = False

    ############################################
    # Init
    ############################################
    def __init__(self):
        pass

    ############################################
    # get run on compartments flag
    ############################################
    def is_loop_on_compartments(self):
        return (self.read_network or
                self.read_compute or
                self.read_database or
                self.read_file_storage or
                self.read_object_storage or
                self.read_load_balancer or
                self.read_email_distribution or
                self.read_resource_management or
                self.read_containers or
                self.read_streams_queues or
                self.read_budgets or
                self.read_monitoring_notifications or
                self.read_data_ai or
                self.read_edge or
                self.read_paas_native or
                self.read_api or
                self.read_function)

    ############################################
    # check if to load basic network (vcn+subnets)
    ############################################
    def is_load_basic_network(self):
        return (self.read_network or
                self.read_compute or
                self.read_database or
                self.read_file_storage or
                self.read_load_balancer or
                self.read_containers or
                self.read_function or
                self.read_api or
                self.read_paas_native)


##########################################################################
# class ShowOCIDomains
##########################################################################
# list_groups
# list_users
# list_dynamic_resource_groups
# list_kmsi_settings
# list_identity_providers
# list_authentication_factor_settings
# list_password_policies
##########################################################################
class ShowOCIDomains(object):

    data = []
    config = {}
    signer = None
    proxy = None
    error = 0
    warning = 0
    read_timeout = 30
    connection_timeout = 30
    skip_identity_user_credential = False
    skip_threads = False
    thread_lock = threading.Lock()

    ##########################################################################
    # init class
    # Creates a new data object
    ##########################################################################
    def __init__(self, config, signer, flags):

        self.data = []
        self.config = config
        self.signer = signer
        self.read_timeout = flags.read_timeout
        self.connection_timeout = flags.connection_timeout
        self.skip_identity_user_credential = flags.skip_identity_user_credential
        self.proxy = flags.proxy
        self.skip_threads = flags.skip_threads

    ##################################################################################
    # get_value function
    ##################################################################################
    def get_value(self, val):
        if not val:
            return ""
        return str(val)

    ##################################################################################
    # get_value value,ocid,ref
    ##################################################################################
    def get_value_ocid_ref(self, val):
        if not val:
            return []

        return [{
            'value': self.get_value(x.value),
            'ocid': self.get_value(x.ocid),
            'ref': self.get_value(x.ref)
        } for x in val]

    ##################################################################################
    # get_date
    # Example of Date 2022-08-20T23:32:54.491Z -> 2022-08-20 23:32
    ##################################################################################
    def get_date(self, val):
        if not val:
            return ""
        return str(val)[0:16].replace("T", " ")

    ##################################################################################
    # __get_api_keys
    ##################################################################################
    def __get_api_keys(self, identity_domain_client, ocid, ext_credential):
        keys = []
        try:
            if ext_credential is not None:
                search_request = oci.identity_domains.models.ApiKeySearchRequest(filter='user.ocid eq "' + self.get_value(ocid) + '"', schemas=["urn:ietf:params:scim:api:messages:2.0:SearchRequest"])
                result = identity_domain_client.search_api_keys(api_key_search_request=search_request)
                for r in result.data.resources:
                    k = {
                        "ocid": r.ocid,
                        "fingerprint": r.fingerprint,
                        "time_created": self.get_date(r.meta.created),
                    }
                    keys.append(k)
            return keys
        except Exception as e:
            self.__print_error("__get_api_keys", e)
            return keys

    ##################################################################################
    # __get_auth_tokens
    ##################################################################################
    def __get_auth_tokens(self, identity_domain_client, ocid, ext_credential):
        keys = []
        try:
            if ext_credential is not None:
                search_request = oci.identity_domains.models.AuthTokenSearchRequest(filter='user.ocid eq "' + self.get_value(ocid) + '"', schemas=["urn:ietf:params:scim:api:messages:2.0:SearchRequest"])
                result = identity_domain_client.search_auth_tokens(auth_token_search_request=search_request)
                for r in result.data.resources:
                    k = {
                        "ocid": r.ocid,
                        "status": r.status,
                        "time_created": self.get_date(r.meta.created),
                        "expires_on": r.expires_on
                    }
                    keys.append(k)
            return keys
        except Exception as e:
            self.__print_error("__get_auth_tokens", e)
            return keys

    ##################################################################################
    # __get_customer_secret_keys
    ##################################################################################
    def __get_customer_secret_keys(self, identity_domain_client, ocid, ext_credential):
        keys = []
        try:
            if ext_credential is not None:
                search_request = oci.identity_domains.models.CustomerSecretKeySearchRequest(filter='user.ocid eq "' + self.get_value(ocid) + '"', schemas=["urn:ietf:params:scim:api:messages:2.0:SearchRequest"])
                result = identity_domain_client.search_customer_secret_keys(customer_secret_key_search_request=search_request)
                for r in result.data.resources:
                    k = {
                        "ocid": r.ocid,
                        "display_name": r.display_name,
                        "description": r.description,
                        "status": r.status,
                        "time_created": self.get_date(r.meta.created),
                        "expires_on": r.expires_on
                    }
                    keys.append(k)
            return keys
        except Exception as e:
            self.__print_error("__get_customer_secret_keys", e)
            return keys

    ##################################################################################
    # __get_o_auth2_client_credentials
    ##################################################################################
    def __get_o_auth2_client_credentials(self, identity_domain_client, ocid, ext_credential):
        keys = []
        try:
            if ext_credential is not None:
                search_request = oci.identity_domains.models.OAuth2ClientCredentialSearchRequest(filter='user.ocid eq "' + self.get_value(ocid) + '"', schemas=["urn:ietf:params:scim:api:messages:2.0:SearchRequest"])
                result = identity_domain_client.search_o_auth2_client_credentials(o_auth2_client_credential_search_request=search_request)
                for r in result.data.resources:
                    print(">> " + str(r))
                    k = {
                        "ocid": r.ocid,
                        "description": r.description,
                        "status": r.status,
                        "time_created": self.get_date(r.meta.created),
                        "expires_on": r.expires_on
                    }
                    keys.append(k)
            return keys
        except Exception as e:
            self.__print_error("__get_o_auth2_client_credentials", e)
            return keys

    ##################################################################################
    # __get_smtp_credentials
    ##################################################################################
    def __get_smtp_credentials(self, identity_domain_client, ocid, ext_credential):
        keys = []
        try:
            if ext_credential is not None:
                search_request = oci.identity_domains.models.SmtpCredentialSearchRequest(filter='user.ocid eq "' + self.get_value(ocid) + '"', schemas=["urn:ietf:params:scim:api:messages:2.0:SearchRequest"])
                result = identity_domain_client.search_smtp_credentials(smtp_credential_search_request=search_request)
                for r in result.data.resources:
                    k = {
                        "ocid": r.ocid,
                        "description": r.description,
                        "status": r.status,
                        "time_created": self.get_date(r.meta.created),
                        "expires_on": r.expires_on
                    }
                    keys.append(k)
            return keys
        except Exception as e:
            self.__print_error("__get_smtp_credentials", e)
            return keys

    ##################################################################################
    # __get_user_db_credentials
    ##################################################################################
    def __get_user_db_credentials(self, identity_domain_client, ocid, ext_credential):
        keys = []
        try:
            if ext_credential is not None:
                search_request = oci.identity_domains.models.UserDbCredentialsSearchRequest(filter='user.ocid eq "' + self.get_value(ocid) + '"', schemas=["urn:ietf:params:scim:api:messages:2.0:SearchRequest"])
                result = identity_domain_client.search_user_db_credentials(user_db_credentials_search_request=search_request)
                for r in result.data.resources:
                    k = {
                        "ocid": r.ocid,
                        "description": r.description,
                        "status": r.status,
                        "time_created": self.get_date(r.meta.created),
                        "expires_on": r.expires_on
                    }
                    keys.append(k)
            return keys
        except Exception as e:
            self.__print_error("__get_user_db_credentials", e)
            return keys

    ##########################################################################
    # print count result for Thread
    ##########################################################################
    def __load_print_thread_cnt(self, header, cnt, start_time, errstr):

        et = time.time() - start_time
        str_time = '{:02d}:{:02d}:{:02d}'.format(round(et // 3600), (round(et % 3600 // 60)), round(et % 60))
        str_cnt = str("(" + str(cnt) + ")").ljust(7)

        if self.skip_threads:
            print(str_cnt + " - " + str_time)
        else:
            # lock for printing
            with self.thread_lock:
                str1 = "--> " + header.ljust(32) + "<-- " + errstr
                str2 = str_cnt + " - " + str_time
                print(str1 + str2)

    ##########################################################################
    # print status message with Threads
    ##########################################################################
    def __load_print_status_with_threads(self, msg):
        if self.skip_threads:
            print("--> " + msg.ljust(32) + "<-- ", end="")
        # else:
            # print("=== Running " + msg + "...")

    ##########################################################################
    # get_tags
    # convert idcs tags to normal OCI tags
    ##########################################################################
    def __get_tags(self, tags, is_defined):
        data = {}
        try:
            if not tags:
                return {}

            # defined_tags
            if is_defined:
                if tags.defined_tags:
                    for tag in tags.defined_tags:

                        if tag.namespace in data:
                            data[tag.namespace][tag.key] = tag.value
                        else:
                            data[tag.namespace] = {tag.key: tag.value}

            # freeform_tags
            else:
                if tags.freeform_tags:
                    for tag in tags.freeform_tags:
                        data[tag.key] = tag.value

            return data
        except Exception as e:
            self.__print_error("__get_tags", e)
            return data

    ##########################################################################
    # print print error
    ##########################################################################
    def __print_error(self, msg, e):
        classname = type(self).__name__

        if 'TooManyRequests' in str(e):
            print(" - TooManyRequests Err in " + msg)
        elif isinstance(e, KeyError):
            print("\nError in " + classname + ":" + msg + ": KeyError " + str(e.args))
        else:
            print("\nError in " + classname + ":" + msg + ": " + str(e))

        self.error += 1

    ##########################################################################
    # check service error to warn instead of error
    ##########################################################################
    def __check_service_error(self, code):
        return ('remote end closed' in str(code).lower() or
                'max retries exceeded' in str(code).lower() or
                'auth' in str(code).lower() or
                'aborted' in str(code).lower() or
                'notfound' in str(code).lower() or
                'closed connection' in str(code).lower() or
                'accessdenied' in str(code).lower() or
                code == 'Forbidden' or
                code == 'TooManyRequests' or
                code == 'NotAuthorizedOrNotFound' or
                code == 'IncorrectState' or
                code == 'LimitExceeded'
                )

    ##########################################################################
    # print auth warning
    ##########################################################################
    def __load_print_auth_warning(self, special_char="a", increase_warning=True):
        if increase_warning:
            self.warning += 1
        print(special_char, end="")

    ##########################################################################
    # check request error if service not exists for region
    ##########################################################################
    def __check_request_error(self, e):

        # service not yet available
        if (
                ('Errno 8' in str(e) and 'NewConnectionError' in str(e)) or
                'Max retries exceeded' in str(e) or
                'HTTPSConnectionPool' in str(e) or
                'not currently available' in str(e) or
                'closed connection' in str(e)
        ):
            print("Service Not Accessible or not yet exist")
            return True

        # if ReadTimeoutError timeout
        if ('ReadTimeoutError' in str(e)):
            print("ReadTimeoutError, Please use higher value with -readtimeout flag !\nError: " + str(e))
            self.error += 1
            return True

        # if Connection TimeoutError timeout
        if ('TimeoutError' in str(e)):
            print("Connection TimeoutError, Please use higher value with -conntimeout flag !\nError: " + str(e))
            self.error += 1
            return True

        return False

    ##########################################################################
    # get Meta Module
    ##########################################################################
    def __load_identity_meta_info(self, meta):
        try:

            if not meta:
                return {}

            return {
                'resource_type': self.get_value(meta.resource_type),
                'created': self.get_date(meta.created),
                'last_modified': self.get_date(meta.last_modified),
                'location': self.get_value(meta.location),
                'version': self.get_value(meta.version)
            }

        except Exception as e:
            self.__print_error("__load_identity_meta_info", e)

    ##########################################################################
    # Pagination main call
    ##########################################################################
    def __list_call_get_all_results(self, list_func_ref, *list_func_args, **list_func_kwargs):

        aggregated_results = []
        for call_result in self.__list_call_get_all_results_generator_domains(list_func_ref, *list_func_args, **list_func_kwargs):
            aggregated_results.extend(call_result.data.resources)
            final_response = oci.Response(call_result.status, call_result.headers, aggregated_results, call_result.request)
        return final_response

    ##########################################################################
    # Pagination result generator
    ##########################################################################
    def __list_call_get_all_results_generator_domains(self, list_func_ref, *list_func_args, **list_func_kwargs):

        keep_paginating = True

        while keep_paginating:
            call_result = oci.retry.DEFAULT_RETRY_STRATEGY.make_retrying_call(list_func_ref, *list_func_args, **list_func_kwargs)
            yield call_result

            start_index = call_result.data.start_index
            total_results = call_result.data.total_results
            items_per_page = call_result.data.items_per_page
            next_index = start_index + items_per_page

            # print("\nCalled " + str(list_func_ref))
            # print("start_index: " + str(start_index) + ", " + "total_results: " + str(total_results) + ", " + "items_per_page: " + str(items_per_page) + ", " + "next_index: " + str(next_index))

            if next_index < total_results:
                list_func_kwargs['start_index'] = next_index
            else:
                keep_paginating = False

##################################################################################
# load_identity_domain_users
##################################################################################
    def __load_identity_domain_users(self, identity_domain_client, domain_name):

        data = []
        errstr = ""
        header = domain_name[0:10] + ".Users"
        self.__load_print_status_with_threads(header)

        start_time = time.time()

        try:
            users = self.__list_call_get_all_results(
                identity_domain_client.list_users,
                attribute_sets=["all"],
                sort_by="UserName",
                count=500,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # oci.identity_domains.models.User
            for var in users:
                if var.delete_in_progress:
                    continue

                if self.skip_threads:
                    print(".", end="")

                user_value = {
                    'id': self.get_value(var.id),
                    'ocid': self.get_value(var.ocid),
                    'display_name': self.get_value(var.display_name),
                    'compartment_ocid': self.get_value(var.compartment_ocid),
                    'external_id': self.get_value(var.external_id),
                    'user_name': self.get_value(var.user_name),
                    'description': self.get_value(var.description),
                    'nick_name': self.get_value(var.nick_name),
                    'title': self.get_value(var.title),
                    'user_type': self.get_value(var.user_type),
                    'locale': self.get_value(var.locale),
                    'preferred_language': self.get_value(var.preferred_language),
                    'timezone': self.get_value(var.timezone),
                    'active': self.get_value(var.active),
                    'schemas': str(','.join(x for x in var.schemas)) if var.schemas else "",
                    'meta': self.__load_identity_meta_info(var.meta),
                    'idcs_prevented_operations': str(','.join(x for x in var.idcs_prevented_operations)) if var.idcs_prevented_operations else "",
                    'idcs_created_by': var.idcs_created_by.value if var.idcs_created_by else "",
                    'idcs_last_modified_by': var.idcs_last_modified_by.value if var.idcs_last_modified_by else "",
                    'family_name': var.name.family_name if var.name else "",
                    'given_name': var.name.given_name if var.name else "",
                    'tags': [{'key': x.key, 'value': x.value} for x in var.tags] if var.tags else [],
                    'freeform_tags': self.__get_tags(var.urn_ietf_params_scim_schemas_oracle_idcs_extension_oci_tags, False),
                    'defined_tags': self.__get_tags(var.urn_ietf_params_scim_schemas_oracle_idcs_extension_oci_tags, True),
                    'phone_numbers': [x.value for x in var.phone_numbers] if var.phone_numbers else [],
                    'ims': [x.value for x in var.ims] if var.ims else [],
                    'emails': [x.value for x in var.emails] if var.emails else [],
                    'entitlements': [x.value for x in var.entitlements] if var.entitlements else [],
                    'x509_certificates': [x.value for x in var.x509_certificates] if var.x509_certificates else [],
                    'groups': [{
                        'value': self.get_value(x.value),
                        'display': self.get_value(x.display),
                        'non_unique_display': self.get_value(x.non_unique_display),
                        'external_id': self.get_value(x.external_id),
                        'type': self.get_value(x.type),
                        'membership_ocid': self.get_value(x.membership_ocid),
                        'ocid': self.get_value(x.ocid),
                        'date_added': self.get_date(x.date_added)
                    } for x in var.groups] if var.groups else [],
                    'ext_user': self.load_identity_domain_users_ext_user(var),
                    'ext_password': self.load_identity_domain_users_ext_password(var),
                    'ext_user_state': self.load_identity_domain_users_ext_user_state(var),
                    'ext_mfa': self.load_identity_domain_users_ext_mfa(var),
                    'ext_posix': self.load_identity_domain_users_ext_posix(var),
                    'ext_adaptive': self.load_identity_domain_users_ext_adaptive(var),
                    'ext_db_user': self.load_identity_domain_users_ext_db_user(var),
                    'ext_db_user_credential': self.load_identity_domain_users_ext_db_user_credential(var),
                    'ext_capabilities': self.load_identity_domain_users_ext_capabilities(var),
                    'roles': [{'value': x.value, 'type': x.type} for x in var.roles] if var.roles else [],
                    'api_keys': [],
                    'customer_secret_keys': [],
                    'auth_tokens': [],
                    'smtp_credentials': [],
                    'o_auth2_client_credentials': [],
                    'db_credentials': [],
                    'allow_self_change': self.load_identity_domain_users_ext_self_change(var)
                }

                ext_credential = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_user_credentials_user

                if ext_credential and not self.skip_identity_user_credential:
                    user_value['api_keys'] = self.__get_api_keys(identity_domain_client, var.ocid, ext_credential)
                    user_value['customer_secret_keys'] = self.__get_customer_secret_keys(identity_domain_client, var.ocid, ext_credential)
                    user_value['auth_tokens'] = self.__get_auth_tokens(identity_domain_client, var.ocid, ext_credential)
                    user_value['smtp_credentials'] = self.__get_smtp_credentials(identity_domain_client, var.ocid, ext_credential)
                    user_value['o_auth2_client_credentials'] = self.__get_o_auth2_client_credentials(identity_domain_client, var.ocid, ext_credential)
                    user_value['db_credentials'] = self.__get_user_db_credentials(identity_domain_client, var.ocid, ext_credential)

                data.append(user_value)

            self.__load_print_thread_cnt(header, len(data), start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
            elif self.__check_service_error(str(e)):
                self.__load_print_auth_warning()
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_domain_users", e)

##################################################################################
# load_identity_domain_users_ext_password
##################################################################################
    def load_identity_domain_users_ext_self_change(self, var):
        data = ""
        try:
            ext_self_change = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_self_change_user

            if ext_self_change:
                data = self.get_date(ext_self_change.allow_self_change)

            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_self_change", e)
            return data

##################################################################################
# load_identity_domain_users_ext_password
##################################################################################
    def load_identity_domain_users_ext_password(self, var):

        try:
            data = {
                'last_successful_set_date': "",
                'cant_change': "",
                'cant_expire': "",
                'must_change': "",
                'expired': "",
                'last_successful_validation_date': "",
                'last_failed_validation_date': "",
                'applicable_password_policy': ""
            }
            ext_password = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_password_state_user

            if ext_password:
                data['last_successful_set_date'] = self.get_date(ext_password.last_successful_set_date)
                data['cant_change'] = self.get_value(ext_password.cant_change)
                data['cant_expire'] = self.get_value(ext_password.cant_expire)
                data['must_change'] = self.get_value(ext_password.must_change)
                data['expired'] = self.get_value(ext_password.expired)
                data['last_successful_validation_date'] = self.get_date(ext_password.last_successful_validation_date)
                data['last_failed_validation_date'] = self.get_date(ext_password.last_failed_validation_date)

                if ext_password.applicable_password_policy:
                    data['applicable_password_policy'] = self.get_value(ext_password.applicable_password_policy.value)

            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_password", e)
            return data

##################################################################################
# load_identity_domain_users_ext_db_user_credential
##################################################################################
    def load_identity_domain_users_ext_db_user_credential(self, var):

        try:
            data = {
                'db_user_name': "",
                'db_login_attempts': ""
            }
            ext_db_user_credential = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_db_credentials_user

            if ext_db_user_credential:
                data['db_user_name'] = self.get_value(ext_db_user_credential.db_user_name)
                data['db_login_attempts'] = self.get_value(ext_db_user_credential.db_login_attempts)

            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_db_user_credential", e)
            return data

##################################################################################
# load_identity_domain_users_ext_adaptive
##################################################################################
    def load_identity_domain_users_ext_adaptive(self, var):

        try:
            data = {
                'risk_level': "",
                'risk_scores': ""
            }
            ext_adaptive = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_adaptive_user

            if ext_adaptive:
                data['risk_level'] = self.get_value(ext_adaptive.risk_level)

                if ext_adaptive.risk_scores:
                    data['risk_scores'] = str(','.join(self.get_value(x.value) for x in ext_adaptive.risk_scores))

            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_adaptive", e)
            return data

##################################################################################
# load_identity_domain_users_ext_posix
##################################################################################
    def load_identity_domain_users_ext_posix(self, var):

        try:
            data = {
                'uid_number': "",
                'gid_number': "",
                'gecos': "",
                'home_directory': "",
                'login_shell': ""
            }
            ext_posix = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_user

            if ext_posix:
                data = {
                    'uid_number': self.get_value(ext_posix.uid_number),
                    'gid_number': self.get_value(ext_posix.gid_number),
                    'gecos': self.get_value(ext_posix.gecos),
                    'home_directory': self.get_value(ext_posix.home_directory),
                    'login_shell': self.get_value(ext_posix.login_shell)
                }
            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_posix", e)
            return data

##################################################################################
# load_identity_domain_users_ext_db_user
##################################################################################
    def load_identity_domain_users_ext_db_user(self, var):

        try:
            data = {
                'is_db_user': "",
                'domain_level_schema': "",
                'instance_level_schema': "",
                'db_global_roles': ""
            }
            ext_db_user = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_db_user_user

            if ext_db_user:
                data = {
                    'is_db_user': self.get_value(ext_db_user.is_db_user),
                    'domain_level_schema': self.get_value(ext_db_user.domain_level_schema),
                    'instance_level_schema': self.get_value(ext_db_user.instance_level_schema),
                    'db_global_roles': str(','.join(x for x in ext_db_user.db_global_roles)) if ext_db_user.db_global_roles else ""
                }
            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_db_user", e)
            return data

##################################################################################
# load_identity_domain_users_ext_user_state
##################################################################################
    def load_identity_domain_users_ext_user_state(self, var):

        try:
            data = {
                'last_successful_login_date': "",
                'previous_successful_login_date': "",
                'last_failed_login_date': "",
                'login_attempts': "",
                'recovery_attempts': "",
                'recovery_enroll_attempts': "",
                'max_concurrent_sessions': "",
                'recovery_locked_date': "",
                'recovery_locked_on': "",
                'locked_date': "",
                'locked_expired': "",
                'locked_on': "",
                'locked_reason': ""
            }
            ext_user_state = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_user_state_user

            if ext_user_state:
                data['last_successful_login_date'] = self.get_date(ext_user_state.last_successful_login_date)
                data['previous_successful_login_date'] = self.get_date(ext_user_state.previous_successful_login_date)
                data['last_failed_login_date'] = self.get_date(ext_user_state.last_failed_login_date)
                data['login_attempts'] = self.get_value(ext_user_state.login_attempts)
                data['recovery_attempts'] = self.get_value(ext_user_state.recovery_attempts)
                data['recovery_enroll_attempts'] = self.get_value(ext_user_state.recovery_enroll_attempts)
                data['max_concurrent_sessions'] = self.get_value(ext_user_state.max_concurrent_sessions)

                if ext_user_state.recovery_locked:
                    data['recovery_locked_date'] = self.get_date(ext_user_state.recovery_locked.lock_date)
                    data['recovery_locked_on'] = self.get_value(ext_user_state.recovery_locked.on)

                if ext_user_state.locked:
                    data['locked_date'] = self.get_date(ext_user_state.locked.lock_date)
                    data['locked_expired'] = self.get_date(ext_user_state.locked.on)
                    data['locked_on'] = self.get_value(ext_user_state.locked.on)
                    data['locked_reason'] = self.get_value(ext_user_state.locked.reason)

            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_user_state", e)
            return data

##################################################################################
# load_identity_domain_users_ext_mfa
##################################################################################
    def load_identity_domain_users_ext_mfa(self, var):

        try:
            data = {
                'preferred_authentication_factor': "",
                'mfa_status': "",
                'preferred_third_party_vendor': "",
                'preferred_authentication_method': "",
                'login_attempts': "",
                'mfa_enabled_on': "",
                'mfa_ignored_apps': ""
            }
            ext_mfa = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_mfa_user

            if ext_mfa:
                data['preferred_authentication_factor'] = self.get_value(ext_mfa.preferred_authentication_factor)
                data['mfa_status'] = self.get_value(ext_mfa.mfa_status)
                data['preferred_third_party_vendor'] = self.get_value(ext_mfa.preferred_third_party_vendor)
                data['preferred_authentication_method'] = self.get_value(ext_mfa.preferred_authentication_method)
                data['login_attempts'] = self.get_value(ext_mfa.login_attempts)
                data['mfa_enabled_on'] = self.get_value(ext_mfa.mfa_enabled_on)

                if ext_mfa.mfa_ignored_apps:
                    data['mfa_ignored_apps'] = str(','.join(self.get_value(x) for x in ext_mfa.mfa_ignored_apps))

            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_mfa", e)
            return data

##################################################################################
# load_identity_domain_users_ext_capabilities
##################################################################################
    def load_identity_domain_users_ext_capabilities(self, var):

        try:
            data = {
                'can_use_api_keys': "",
                'can_use_auth_tokens': "",
                'can_use_console_password': "",
                'can_use_customer_secret_keys': "",
                'can_use_o_auth2_client_credentials': "",
                'can_use_smtp_credentials': "",
                'can_use_db_credentials': ""
            }
            ext_capabilities = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_capabilities_user

            if ext_capabilities:
                data = {
                    'can_use_api_keys': self.get_value(ext_capabilities.can_use_api_keys),
                    'can_use_auth_tokens': self.get_value(ext_capabilities.can_use_auth_tokens),
                    'can_use_console_password': self.get_value(ext_capabilities.can_use_console_password),
                    'can_use_customer_secret_keys': self.get_value(ext_capabilities.can_use_customer_secret_keys),
                    'can_use_o_auth2_client_credentials': self.get_value(ext_capabilities.can_use_o_auth2_client_credentials),
                    'can_use_smtp_credentials': self.get_value(ext_capabilities.can_use_smtp_credentials),
                    'can_use_db_credentials': self.get_value(ext_capabilities.can_use_db_credentials)
                }
            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_capabilities", e)
            return data

##################################################################################
# load_identity_domain_users_ext_user
##################################################################################
    def load_identity_domain_users_ext_user(self, var):
        data = {}
        try:
            data = {
                'is_federated_user': "",
                'is_authentication_delegated': "",
                'status': "",
                'provider': "",
                'creation_mechanism': "",
                'do_not_show_getting_started': "",
                'bypass_notification': "",
                'is_account_recovery_enrolled': "",
                'account_recovery_required': "",
                'user_flow_controlled_by_external_client': "",
                'is_group_membership_normalized': "",
                'is_group_membership_synced_to_users_groups': ""
            }

            ext_user = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_user_user
            if ext_user:
                data = {
                    'is_federated_user': self.get_value(ext_user.is_federated_user),
                    'is_authentication_delegated': self.get_value(ext_user.is_authentication_delegated),
                    'status': self.get_value(ext_user.status),
                    'provider': self.get_value(ext_user.provider),
                    'creation_mechanism': self.get_value(ext_user.creation_mechanism),
                    'do_not_show_getting_started': self.get_value(ext_user.do_not_show_getting_started),
                    'bypass_notification': self.get_value(ext_user.bypass_notification),
                    'is_account_recovery_enrolled': self.get_value(ext_user.is_account_recovery_enrolled),
                    'account_recovery_required': self.get_value(ext_user.account_recovery_required),
                    'user_flow_controlled_by_external_client': self.get_value(ext_user.user_flow_controlled_by_external_client),
                    'is_group_membership_normalized': self.get_value(ext_user.is_group_membership_normalized),
                    'is_group_membership_synced_to_users_groups': self.get_value(ext_user.is_group_membership_synced_to_users_groups)
                }
            return data

        except Exception as e:
            self.__print_error("load_identity_domain_users_ext_capabilities", e)
            return data

##################################################################################
# load_identity_domain_groups
##################################################################################
    def __load_identity_domain_groups(self, identity_domain_client, domain_name):
        data = []

        errstr = ""
        header = domain_name[0:10] + ".Groups"
        self.__load_print_status_with_threads(header)

        start_time = time.time()

        try:
            groups = self.__list_call_get_all_results(
                identity_domain_client.list_groups,
                attribute_sets=["all"],
                sort_by="DisplayName",
                count=500,
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # oci.identity_domains.models.Group
            for var in groups:
                if var.delete_in_progress:
                    continue
                if self.skip_threads:
                    print(".", end="")

                ext_group = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_group_group
                ext_posix = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_posix_group
                ext_req_group = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_requestable_group
                ext_dbcs_group = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_dbcs_group
                ext_dynamic_group = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_dynamic_group

                data.append({
                    'id': self.get_value(var.id),
                    'ocid': self.get_value(var.ocid),
                    'display_name': self.get_value(var.display_name),
                    'schemas': str(','.join(x for x in var.schemas)) if var.schemas else "",
                    'meta': self.__load_identity_meta_info(var.meta),
                    'idcs_created_by': var.idcs_created_by.value if var.idcs_created_by else "",
                    'idcs_last_modified_by': var.idcs_last_modified_by.value if var.idcs_last_modified_by else "",
                    'idcs_prevented_operations': str(','.join(x for x in var.idcs_prevented_operations)) if var.idcs_prevented_operations else "",
                    'idcs_last_upgraded_in_release': self.get_value(var.idcs_last_upgraded_in_release),
                    'external_id': self.get_value(var.external_id),
                    'compartment_ocid': self.get_value(var.compartment_ocid),
                    'non_unique_display_name': self.get_value(var.non_unique_display_name),
                    'tags': [{'key': x.key, 'value': x.value} for x in var.tags] if var.tags else [],
                    'freeform_tags': self.__get_tags(var.urn_ietf_params_scim_schemas_oracle_idcs_extension_oci_tags, False),
                    'defined_tags': self.__get_tags(var.urn_ietf_params_scim_schemas_oracle_idcs_extension_oci_tags, True),
                    'members': [{
                        'value': self.get_value(x.value),
                        'date_added': self.get_date(x.date_added),
                        'ocid': self.get_value(x.ocid),
                        'membership_ocid': self.get_value(x.membership_ocid),
                        'ref': self.get_value(x.ref),
                        'display': self.get_value(x.display),
                        'type': self.get_value(x.type),
                        'name': self.get_value(x.name)
                    } for x in var.members] if var.members else [],
                    'ext_group': {
                        'description': self.get_value(ext_group.description) if ext_group else "",
                        'creation_mechanism': self.get_value(ext_group.creation_mechanism) if ext_group else "",
                        'password_policy': self.get_value(ext_group.password_policy.value) if ext_group and ext_group.password_policy else "",
                        'synced_from_app': self.get_value(ext_group.synced_from_app.value) if ext_group and ext_group.synced_from_app else "",
                        'grants': str(','.join(x.value for x in ext_group.grants)) if ext_group and ext_group.grants else "",
                        'owners': str(','.join(x.value for x in ext_group.owners)) if ext_group and ext_group.owners else "",
                        'app_roles': str(','.join(x.value for x in ext_group.app_roles)) if ext_group and ext_group.app_roles else ""
                    },
                    'ext_dbcs_group': {
                        'instance_level_schema_names': str(','.join(x.db_instance_id + ":" + x.schema_name for x in ext_dbcs_group.instance_level_schema_names)) if ext_dbcs_group and ext_dbcs_group.instance_level_schema_names else "",
                        'domain_level_schema_names': str(','.join(x.domain_name + ":" + x.schema_name for x in ext_dbcs_group.domain_level_schema_names)) if ext_dbcs_group and ext_dbcs_group.domain_level_schema_names else "",
                        'domain_level_schema': self.get_value(ext_dbcs_group.domain_level_schema) if ext_dbcs_group else "",
                        'instance_level_schema': self.get_value(ext_dbcs_group.instance_level_schema) if ext_dbcs_group else ""
                    },
                    'ext_dynamic_group': {
                        'membership_type': self.get_value(ext_dynamic_group.membership_type) if ext_dynamic_group else "",
                        'membership_rule': self.get_value(ext_dynamic_group.membership_rule) if ext_dynamic_group else ""
                    },
                    'gid_number': self.get_value(ext_posix.gid_number) if ext_posix else "",
                    'requestable_group': self.get_value(ext_req_group.requestable) if ext_req_group else ""
                })

            self.__load_print_thread_cnt(header, len(data), start_time, errstr)
            return data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_domain_groups", e)

##################################################################################
# __load_identity_domain_dynamic_resource_groups
##################################################################################
    def __load_identity_domain_dynamic_resource_groups(self, identity_domain_client, domain_name):
        data = []

        errstr = ""
        header = domain_name[0:10] + ".Dynamic Groups"
        self.__load_print_status_with_threads(header)

        start_time = time.time()

        try:
            groups = self.__list_call_get_all_results(
                identity_domain_client.list_dynamic_resource_groups,
                attribute_sets=["all"],
                sort_by="DisplayName",
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # oci.identity_domains.models.DynamicResourceGroup
            for var in groups:
                if var.delete_in_progress:
                    continue
                if self.skip_threads:
                    print(".", end="")

                data.append({
                    'id': self.get_value(var.id),
                    'ocid': self.get_value(var.ocid),
                    'schemas': str(','.join(x for x in var.schemas)) if var.schemas else "",
                    'meta': self.__load_identity_meta_info(var.meta),
                    'idcs_created_by': var.idcs_created_by.value if var.idcs_created_by else "",
                    'idcs_last_modified_by': var.idcs_last_modified_by.value if var.idcs_last_modified_by else "",
                    'idcs_prevented_operations': str(','.join(x for x in var.idcs_prevented_operations)) if var.idcs_prevented_operations else "",
                    'tags': [{'key': x.key, 'value': x.value} for x in var.tags] if var.tags else [],
                    'idcs_last_upgraded_in_release': self.get_value(var.idcs_last_upgraded_in_release),
                    'compartment_ocid': self.get_value(var.compartment_ocid),
                    'matching_rule': var.matching_rule,
                    'display_name': self.get_value(var.display_name),
                    'description': self.get_value(var.description),
                    'grants': [{
                        'value': self.get_value(x.value),
                        'ref': self.get_value(x.ref),
                        'app_id': self.get_value(x.app_id),
                        'grant_mechanism': self.get_value(x.grant_mechanism)
                    } for x in var.grants] if var.grants else [],
                    'dynamic_group_app_roles': [{
                        'value': self.get_value(x.value),
                        'ref': self.get_value(x.ref),
                        'display': self.get_value(x.display),
                        'app_id': self.get_value(x.app_id),
                        'app_name': self.get_value(x.app_name),
                        'admin_role': self.get_value(x.admin_role),
                        'legacy_group_name': self.get_value(x.legacy_group_name)
                    } for x in var.dynamic_group_app_roles] if var.dynamic_group_app_roles else [],
                    'freeform_tags': self.__get_tags(var.urn_ietf_params_scim_schemas_oracle_idcs_extension_oci_tags, False),
                    'defined_tags': self.__get_tags(var.urn_ietf_params_scim_schemas_oracle_idcs_extension_oci_tags, True)
                })

            self.__load_print_thread_cnt(header, len(data), start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
            elif self.__check_service_error(str(e)):
                self.__load_print_auth_warning()
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_domain_dynamic_resource_groups", e)

##################################################################################
# __load_identity_domain_identity_providers
##################################################################################
    def __load_identity_domain_identity_providers(self, identity_domain_client, domain_name):
        data = []

        errstr = ""
        header = domain_name[0:10] + ".IDPs"
        self.__load_print_status_with_threads(header)

        start_time = time.time()

        try:
            groups = self.__list_call_get_all_results(
                identity_domain_client.list_identity_providers,
                attribute_sets=["all"],
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # oci.identity_domains.models.IdentityProvider
            for var in groups:
                if var.delete_in_progress:
                    continue

                if self.skip_threads:
                    print(".", end="")

                ext_social_idp = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_social_identity_provider
                ext_x509_idp = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_x509_identity_provider

                data.append({
                    'id': self.get_value(var.id),
                    'ocid': self.get_value(var.ocid),
                    'schemas': str(','.join(x for x in var.schemas)) if var.schemas else "",
                    'meta': self.__load_identity_meta_info(var.meta),
                    'idcs_created_by': var.idcs_created_by.value if var.idcs_created_by else "",
                    'idcs_last_modified_by': var.idcs_last_modified_by.value if var.idcs_last_modified_by else "",
                    'idcs_prevented_operations': str(','.join(x for x in var.idcs_prevented_operations)) if var.idcs_prevented_operations else "",
                    'tags': [{'key': x.key, 'value': x.value} for x in var.tags] if var.tags else [],
                    'idcs_last_upgraded_in_release': self.get_value(var.idcs_last_upgraded_in_release),
                    'compartment_ocid': self.get_value(var.compartment_ocid),
                    'external_id': self.get_value(var.external_id),
                    'partner_name': self.get_value(var.partner_name),
                    'description': self.get_value(var.description),
                    'metadata': self.get_value(var.metadata),
                    'partner_provider_id': self.get_value(var.partner_provider_id),
                    'tenant_provider_id': self.get_value(var.tenant_provider_id),
                    'succinct_id': self.get_value(var.succinct_id),
                    'idp_sso_url': self.get_value(var.idp_sso_url),
                    'logout_request_url': self.get_value(var.logout_request_url),
                    'logout_response_url': self.get_value(var.logout_response_url),
                    'signing_certificate': self.get_value(var.signing_certificate),
                    'encryption_certificate': self.get_value(var.encryption_certificate),
                    'name_id_format': self.get_value(var.name_id_format),
                    'include_signing_cert_in_signature': self.get_value(var.include_signing_cert_in_signature),
                    'authn_request_binding': self.get_value(var.authn_request_binding),
                    'logout_binding': self.get_value(var.logout_binding),
                    'logout_enabled': self.get_value(var.logout_enabled),
                    'signature_hash_algorithm': self.get_value(var.signature_hash_algorithm),
                    'enabled': self.get_value(var.enabled),
                    'icon_url': self.get_value(var.icon_url),
                    'shown_on_login_page': self.get_value(var.shown_on_login_page),
                    'jit_user_prov_enabled': self.get_value(var.jit_user_prov_enabled),
                    'jit_user_prov_group_assertion_attribute_enabled': self.get_value(var.jit_user_prov_group_assertion_attribute_enabled),
                    'jit_user_prov_group_static_list_enabled': self.get_value(var.jit_user_prov_group_static_list_enabled),
                    'jit_user_prov_create_user_enabled': self.get_value(var.jit_user_prov_create_user_enabled),
                    'jit_user_prov_attribute_update_enabled': self.get_value(var.jit_user_prov_attribute_update_enabled),
                    'jit_user_prov_group_assignment_method': self.get_value(var.jit_user_prov_group_assignment_method),
                    'jit_user_prov_group_mapping_mode': self.get_value(var.jit_user_prov_group_mapping_mode),
                    'jit_user_prov_group_mappings': [{
                        'value': self.get_value(x.value),
                        'ref': self.get_value(x.ref),
                        'idp_group': self.get_value(x.idp_group)
                    } for x in var.jit_user_prov_group_mappings] if var.jit_user_prov_group_mappings else [],
                    'jit_user_prov_group_saml_attribute_name': self.get_value(var.jit_user_prov_group_saml_attribute_name),
                    'service_instance_identifier': self.get_value(var.service_instance_identifier),
                    'user_mapping_method': self.get_value(var.user_mapping_method),
                    'user_mapping_store_attribute': self.get_value(var.user_mapping_store_attribute),
                    'assertion_attribute': self.get_value(var.assertion_attribute),
                    'type': self.get_value(var.type),
                    'require_force_authn': self.get_value(var.require_force_authn),
                    'requires_encrypted_assertion': self.get_value(var.requires_encrypted_assertion),
                    'saml_ho_k_required': self.get_value(var.saml_ho_k_required),
                    'requested_authentication_context': var.requested_authentication_context,
                    'jit_user_prov_ignore_error_on_absent_groups': self.get_value(var.jit_user_prov_ignore_error_on_absent_groups),
                    'jit_user_prov_attributes': self.get_value(var.jit_user_prov_attributes.value) if var.jit_user_prov_attributes else "",
                    'jit_user_prov_assigned_groups': self.get_value(var.jit_user_prov_assigned_groups.value) if var.jit_user_prov_assigned_groups else "",
                    'correlation_policy': self.get_value(var.correlation_policy.value) if var.correlation_policy else "",
                    'ext_social_idp': {
                        'account_linking_enabled': self.get_value(ext_social_idp.account_linking_enabled) if ext_social_idp else "",
                        'registration_enabled': self.get_value(ext_social_idp.registration_enabled) if ext_social_idp else "",
                        'status': self.get_value(ext_social_idp.status) if ext_social_idp else "",
                        'authz_url': self.get_value(ext_social_idp.authz_url) if ext_social_idp else "",
                        'access_token_url': self.get_value(ext_social_idp.access_token_url) if ext_social_idp else "",
                        'profile_url': self.get_value(ext_social_idp.profile_url) if ext_social_idp else "",
                        'scope': ext_social_idp.scope if ext_social_idp else [],
                        'admin_scope': ext_social_idp.admin_scope if ext_social_idp else [],
                        'consumer_key': self.get_value(ext_social_idp.consumer_key) if ext_social_idp else "",
                        'consumer_secret': self.get_value(ext_social_idp.consumer_secret) if ext_social_idp else "",
                        'service_provider_name': self.get_value(ext_social_idp.service_provider_name) if ext_social_idp else "",
                        'clock_skew_in_seconds': self.get_value(ext_social_idp.clock_skew_in_seconds) if ext_social_idp else "",
                        'redirect_url': self.get_value(ext_social_idp.redirect_url) if ext_social_idp else "",
                        'discovery_url': self.get_value(ext_social_idp.discovery_url) if ext_social_idp else "",
                        'client_credential_in_payload': self.get_value(ext_social_idp.client_credential_in_payload) if ext_social_idp else "",
                        'id_attribute': self.get_value(ext_social_idp.id_attribute) if ext_social_idp else ""
                    },
                    'ext_x509_idp': {
                        'cert_match_attribute': self.get_value(ext_x509_idp.cert_match_attribute) if ext_x509_idp else "",
                        'user_match_attribute': self.get_value(ext_x509_idp.user_match_attribute) if ext_x509_idp else "",
                        'other_cert_match_attribute': self.get_value(ext_x509_idp.other_cert_match_attribute) if ext_x509_idp else "",
                        'signing_certificate_chain': self.get_value(ext_x509_idp.signing_certificate_chain) if ext_x509_idp else "",
                        'ocsp_server_name': self.get_value(ext_x509_idp.ocsp_server_name) if ext_x509_idp else "",
                        'ocsp_responder_url': self.get_value(ext_x509_idp.ocsp_responder_url) if ext_x509_idp else "",
                        'ocsp_allow_unknown_response_status': self.get_value(ext_x509_idp.ocsp_allow_unknown_response_status) if ext_x509_idp else "",
                        'ocsp_revalidate_time': self.get_value(ext_x509_idp.ocsp_revalidate_time) if ext_x509_idp else "",
                        'ocsp_enable_signed_response': self.get_value(ext_x509_idp.ocsp_enable_signed_response) if ext_x509_idp else "",
                        'ocsp_trust_cert_chain': self.get_value(ext_x509_idp.ocsp_trust_cert_chain) if ext_x509_idp else "",
                        'crl_enabled': self.get_value(ext_x509_idp.crl_enabled) if ext_x509_idp else "",
                        'crl_check_on_ocsp_failure_enabled': self.get_value(ext_x509_idp.crl_check_on_ocsp_failure_enabled) if ext_x509_idp else "",
                        'crl_location': self.get_value(ext_x509_idp.crl_location) if ext_x509_idp else "",
                        'crl_reload_duration': self.get_value(ext_x509_idp.crl_reload_duration) if ext_x509_idp else ""
                    }
                })

            self.__load_print_thread_cnt(header, len(data), start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
            elif self.__check_service_error(str(e)):
                self.__load_print_auth_warning()
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_domain_identity_providers", e)

##################################################################################
# __load_identity_domain_kmsi_setting
##################################################################################
    def __load_identity_domain_kmsi_setting(self, identity_domain_client, domain_name):
        data = []

        errstr = ""
        header = domain_name[0:10] + ".Kmsi Setting"
        self.__load_print_status_with_threads(header)

        start_time = time.time()

        try:
            groups = self.__list_call_get_all_results(
                identity_domain_client.list_kmsi_settings,
                attribute_sets=["all"],
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # oci.identity_domains.models.DynamicResourceGroup
            for var in groups:
                if var.delete_in_progress:
                    continue
                if self.skip_threads:
                    print(".", end="")

                data.append({
                    'id': self.get_value(var.id),
                    'ocid': self.get_value(var.ocid),
                    'schemas': str(','.join(x for x in var.schemas)) if var.schemas else "",
                    'meta': self.__load_identity_meta_info(var.meta),
                    'idcs_created_by': var.idcs_created_by.value if var.idcs_created_by else "",
                    'idcs_last_modified_by': var.idcs_last_modified_by.value if var.idcs_last_modified_by else "",
                    'idcs_prevented_operations': str(','.join(x for x in var.idcs_prevented_operations)) if var.idcs_prevented_operations else "",
                    'tags': [{'key': x.key, 'value': x.value} for x in var.tags] if var.tags else [],
                    'idcs_last_upgraded_in_release': self.get_value(var.idcs_last_upgraded_in_release),
                    'compartment_ocid': self.get_value(var.compartment_ocid),
                    'external_id': self.get_value(var.external_id),
                    'token_validity_in_days': self.get_value(var.token_validity_in_days),
                    'last_used_validity_in_days': self.get_value(var.last_used_validity_in_days),
                    'max_allowed_sessions': self.get_value(var.max_allowed_sessions),
                    'kmsi_feature_enabled': self.get_value(var.kmsi_feature_enabled),
                    'kmsi_prompt_enabled': self.get_value(var.kmsi_prompt_enabled),
                    'tou_prompt_disabled': self.get_value(var.tou_prompt_disabled),
                    'last_enabled_on': self.get_date(var.last_enabled_on)
                })

            self.__load_print_thread_cnt(header, len(data), start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
            elif self.__check_service_error(str(e)):
                self.__load_print_auth_warning()
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_domain_kmsi_setting", e)

##################################################################################
# __load_identity_domain_authentication_factor_settings
##################################################################################
    def __load_identity_domain_authentication_factor_settings(self, identity_domain_client, domain_name):
        data = []

        errstr = ""
        header = domain_name[0:10] + ".AuthN Factors"
        self.__load_print_status_with_threads(header)

        start_time = time.time()

        try:
            groups = self.__list_call_get_all_results(
                identity_domain_client.list_authentication_factor_settings,
                attribute_sets=["all"],
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # oci.identity_domains.models.AuthenticationFactorSetting
            for var in groups:
                if var.delete_in_progress:
                    continue
                if self.skip_threads:
                    print(".", end="")

                ext_third_party_auth_factor = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_third_party_authentication_factor_settings
                ext_fido_auth_factor = var.urn_ietf_params_scim_schemas_oracle_idcs_extension_fido_authentication_factor_settings

                data.append({
                    'id': self.get_value(var.id),
                    'ocid': self.get_value(var.ocid),
                    'schemas': str(','.join(x for x in var.schemas)) if var.schemas else "",
                    'meta': self.__load_identity_meta_info(var.meta),
                    'idcs_created_by': var.idcs_created_by.value if var.idcs_created_by else "",
                    'idcs_last_modified_by': var.idcs_last_modified_by.value if var.idcs_last_modified_by else "",
                    'idcs_prevented_operations': str(','.join(x for x in var.idcs_prevented_operations)) if var.idcs_prevented_operations else "",
                    'tags': [{'key': x.key, 'value': x.value} for x in var.tags] if var.tags else [],
                    'idcs_last_upgraded_in_release': self.get_value(var.idcs_last_upgraded_in_release),
                    'compartment_ocid': self.get_value(var.compartment_ocid),
                    'email_enabled': self.get_value(var.email_enabled),
                    'sms_enabled': self.get_value(var.sms_enabled),
                    'phone_call_enabled': self.get_value(var.phone_call_enabled),
                    'totp_enabled': self.get_value(var.totp_enabled),
                    'push_enabled': self.get_value(var.push_enabled),
                    'bypass_code_enabled': self.get_value(var.bypass_code_enabled),
                    'security_questions_enabled': self.get_value(var.security_questions_enabled),
                    'fido_authenticator_enabled': self.get_value(var.fido_authenticator_enabled),
                    'yubico_otp_enabled': self.get_value(var.yubico_otp_enabled),
                    'mfa_enrollment_type': self.get_value(var.mfa_enrollment_type),
                    'mfa_enabled_category': self.get_value(var.mfa_enabled_category),
                    'hide_backup_factor_enabled': self.get_value(var.hide_backup_factor_enabled),
                    'auto_enroll_email_factor_disabled': self.get_value(var.auto_enroll_email_factor_disabled),
                    'user_enrollment_disabled_factors': var.user_enrollment_disabled_factors,
                    'email_link_enabled': self.get_value(var.email_settings.email_link_enabled) if var.email_settings else "",
                    'third_party_factor_duo_security': self.get_value(var.third_party_factor.duo_security) if var.third_party_factor else "",
                    'notification_settings_pull_enabled': self.get_value(var.notification_settings.pull_enabled) if var.notification_settings else "",
                    'identity_store_settings_mobile_number_enabled': self.get_value(var.identity_store_settings.mobile_number_enabled) if var.identity_store_settings else "",
                    'bypass_code_settings': {
                        'self_service_generation_enabled': self.get_value(var.bypass_code_settings.self_service_generation_enabled) if var.bypass_code_settings else "",
                        'help_desk_generation_enabled': self.get_value(var.bypass_code_settings.help_desk_generation_enabled) if var.bypass_code_settings else "",
                        'length': self.get_value(var.bypass_code_settings.length) if var.bypass_code_settings else "",
                        'max_active': self.get_value(var.bypass_code_settings.max_active) if var.bypass_code_settings else "",
                        'help_desk_max_usage': self.get_value(var.bypass_code_settings.help_desk_max_usage) if var.bypass_code_settings else ""
                    },
                    'client_app_settings': {
                        'min_pin_length': self.get_value(var.client_app_settings.min_pin_length) if var.client_app_settings else "",
                        'max_failures_before_warning': self.get_value(var.client_app_settings.max_failures_before_warning) if var.client_app_settings else "",
                        'max_failures_before_lockout': self.get_value(var.client_app_settings.max_failures_before_lockout) if var.client_app_settings else "",
                        'initial_lockout_period_in_secs': self.get_value(var.client_app_settings.initial_lockout_period_in_secs) if var.client_app_settings else "",
                        'lockout_escalation_pattern': self.get_value(var.client_app_settings.lockout_escalation_pattern) if var.client_app_settings else "",
                        'max_lockout_interval_in_secs': self.get_value(var.client_app_settings.max_lockout_interval_in_secs) if var.client_app_settings else "",
                        'request_signing_algo': self.get_value(var.client_app_settings.request_signing_algo) if var.client_app_settings else "",
                        'policy_update_freq_in_days': self.get_value(var.client_app_settings.policy_update_freq_in_days) if var.client_app_settings else "",
                        'key_pair_length': self.get_value(var.client_app_settings.key_pair_length) if var.client_app_settings else "",
                        'device_protection_policy': self.get_value(var.client_app_settings.device_protection_policy) if var.client_app_settings else "",
                        'unlock_app_for_each_request_enabled': self.get_value(var.client_app_settings.unlock_app_for_each_request_enabled) if var.client_app_settings else "",
                        'unlock_on_app_start_enabled': self.get_value(var.client_app_settings.unlock_on_app_start_enabled) if var.client_app_settings else "",
                        'unlock_app_interval_in_secs': self.get_value(var.client_app_settings.unlock_app_interval_in_secs) if var.client_app_settings else "",
                        'shared_secret_encoding': self.get_value(var.client_app_settings.shared_secret_encoding) if var.client_app_settings else "",
                        'unlock_on_app_foreground_enabled': self.get_value(var.client_app_settings.unlock_on_app_foreground_enabled) if var.client_app_settings else ""
                    },
                    'endpoint_restrictions': {
                        'max_enrolled_devices': self.get_value(var.endpoint_restrictions.max_enrolled_devices) if var.endpoint_restrictions else "",
                        'max_trusted_endpoints': self.get_value(var.endpoint_restrictions.max_trusted_endpoints) if var.endpoint_restrictions else "",
                        'max_endpoint_trust_duration_in_days': self.get_value(var.endpoint_restrictions.max_endpoint_trust_duration_in_days) if var.endpoint_restrictions else "",
                        'trusted_endpoints_enabled': self.get_value(var.endpoint_restrictions.trusted_endpoints_enabled) if var.endpoint_restrictions else "",
                        'max_incorrect_attempts': self.get_value(var.endpoint_restrictions.max_incorrect_attempts) if var.endpoint_restrictions else ""
                    },
                    'totp_settings': {
                        'hashing_algorithm': self.get_value(var.totp_settings.hashing_algorithm) if var.totp_settings else "",
                        'passcode_length': self.get_value(var.totp_settings.passcode_length) if var.totp_settings else "",
                        'key_refresh_interval_in_days': self.get_value(var.totp_settings.key_refresh_interval_in_days) if var.totp_settings else "",
                        'time_step_in_secs': self.get_value(var.totp_settings.time_step_in_secs) if var.totp_settings else "",
                        'time_step_tolerance': self.get_value(var.totp_settings.time_step_tolerance) if var.totp_settings else "",
                        'sms_otp_validity_duration_in_mins': self.get_value(var.totp_settings.sms_otp_validity_duration_in_mins) if var.totp_settings else "",
                        'jwt_validity_duration_in_secs': self.get_value(var.totp_settings.jwt_validity_duration_in_secs) if var.totp_settings else "",
                        'sms_passcode_length': self.get_value(var.totp_settings.sms_passcode_length) if var.totp_settings else "",
                        'email_otp_validity_duration_in_mins': self.get_value(var.totp_settings.email_otp_validity_duration_in_mins) if var.totp_settings else "",
                        'email_passcode_length': self.get_value(var.totp_settings.email_passcode_length) if var.totp_settings else ""
                    },
                    'third_party_duo_security_settings': self.get_value(ext_third_party_auth_factor.duo_security_settings) if ext_third_party_auth_factor else "",
                    'compliance_policy': [{
                        'name': self.get_value(x.name),
                        'action': self.get_value(x.action),
                        'value': self.get_value(x.value)
                    } for x in var.compliance_policy] if var.compliance_policy else [],
                    'ext_fido_auth_factor': {
                        'attestation': self.get_value(ext_fido_auth_factor.attestation) if ext_fido_auth_factor else "",
                        'authenticator_selection_attachment': self.get_value(ext_fido_auth_factor.authenticator_selection_attachment) if ext_fido_auth_factor else "",
                        'authenticator_selection_user_verification': self.get_value(ext_fido_auth_factor.authenticator_selection_user_verification) if ext_fido_auth_factor else "",
                        'authenticator_selection_resident_key': self.get_value(ext_fido_auth_factor.authenticator_selection_resident_key) if ext_fido_auth_factor else "",
                        'timeout': self.get_value(ext_fido_auth_factor.timeout) if ext_fido_auth_factor else "",
                        'authenticator_selection_require_resident_key': self.get_value(ext_fido_auth_factor.authenticator_selection_require_resident_key) if ext_fido_auth_factor else "",
                        'public_key_types': self.get_value(ext_fido_auth_factor.public_key_types) if ext_fido_auth_factor else "",
                        'exclude_credentials': self.get_value(ext_fido_auth_factor.exclude_credentials) if ext_fido_auth_factor else "",
                        'domain_validation_level': self.get_value(ext_fido_auth_factor.domain_validation_level) if ext_fido_auth_factor else ""
                    }
                })

            self.__load_print_thread_cnt(header, len(data), start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
            elif self.__check_service_error(str(e)):
                self.__load_print_auth_warning()
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_domain_authentication_factor_settings", e)

##################################################################################
# __load_identity_domain_password_policies
##################################################################################
    def __load_identity_domain_password_policies(self, identity_domain_client, domain_name):

        data = []

        errstr = ""
        header = domain_name[0:10] + ".Password Policies"
        self.__load_print_status_with_threads(header)

        start_time = time.time()
        try:
            policies = self.__list_call_get_all_results(
                identity_domain_client.list_password_policies,
                attribute_sets=["all"],
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data
            # oci.identity_domains.models.PasswordPolicy
            for var in policies:
                if var.delete_in_progress:
                    continue

                if self.skip_threads:
                    print(".", end="")

                data.append({
                    'id': self.get_value(var.id),
                    'ocid': self.get_value(var.ocid),
                    'schemas': str(','.join(x for x in var.schemas)) if var.schemas else "",
                    'meta': self.__load_identity_meta_info(var.meta),
                    'idcs_created_by': var.idcs_created_by.value if var.idcs_created_by else "",
                    'idcs_last_modified_by': var.idcs_last_modified_by.value if var.idcs_last_modified_by else "",
                    'idcs_prevented_operations': str(','.join(x for x in var.idcs_prevented_operations)) if var.idcs_prevented_operations else "",
                    'tags': [{'key': x.key, 'value': x.value} for x in var.tags] if var.tags else [],
                    'idcs_last_upgraded_in_release': self.get_value(var.idcs_last_upgraded_in_release),
                    'compartment_ocid': self.get_value(var.compartment_ocid),
                    'domain_ocid': self.get_value(var.domain_ocid),
                    'external_id': self.get_value(var.external_id),
                    'name': self.get_value(var.name),
                    'description': self.get_value(var.description),
                    'allowed_chars': self.get_value(var.allowed_chars),
                    'configured_password_policy_rules': [{
                        'key': x.key,
                        'value': x.value
                    } for x in var.configured_password_policy_rules] if var.configured_password_policy_rules else [],
                    'dictionary_delimiter': self.get_value(var.dictionary_delimiter),
                    'dictionary_location': self.get_value(var.dictionary_location),
                    'dictionary_word_disallowed': self.get_value(var.dictionary_word_disallowed),
                    'disallowed_chars': self.get_value(var.disallowed_chars),
                    'disallowed_substrings': self.get_value(var.disallowed_substrings),
                    'first_name_disallowed': self.get_value(var.first_name_disallowed),
                    'force_password_reset': self.get_value(var.force_password_reset),
                    'groups': [{
                        'display': x.display,
                        'ref': x.ref,
                        'value': x.value
                    } for x in var.groups] if var.groups else [],
                    'last_name_disallowed': self.get_value(var.last_name_disallowed),
                    'lockout_duration': self.get_value(var.lockout_duration),
                    'max_incorrect_attempts': self.get_value(var.max_incorrect_attempts),
                    'max_length': self.get_value(var.max_length),
                    'max_repeated_chars': self.get_value(var.max_repeated_chars),
                    'max_special_chars': self.get_value(var.max_special_chars),
                    'min_alpha_numerals': self.get_value(var.min_alpha_numerals),
                    'min_alphas': self.get_value(var.min_alphas),
                    'min_length': self.get_value(var.min_length),
                    'min_lower_case': self.get_value(var.min_lower_case),
                    'min_numerals': self.get_value(var.min_numerals),
                    'min_password_age': self.get_value(var.min_password_age),
                    'min_special_chars': self.get_value(var.min_special_chars),
                    'min_unique_chars': self.get_value(var.min_unique_chars),
                    'min_upper_case': self.get_value(var.min_upper_case),
                    'num_passwords_in_history': self.get_value(var.num_passwords_in_history),
                    'password_expire_warning': self.get_value(var.password_expire_warning),
                    'password_expires_after': self.get_value(var.password_expires_after),
                    'password_strength': self.get_value(var.password_strength),
                    'priority': self.get_value(var.priority),
                    'required_chars': self.get_value(var.required_chars),
                    'starts_with_alphabet': self.get_value(var.starts_with_alphabet),
                    'user_name_disallowed': self.get_value(var.user_name_disallowed)
                })

            self.__load_print_thread_cnt(header, len(data), start_time, errstr)
            return data

        except oci.exceptions.ServiceError as e:
            if self.__check_service_error(e.code):
                self.__load_print_auth_warning()
            else:
                raise
        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return
            raise
        except Exception as e:
            self.__print_error("__load_identity_domain_password_policies", e)

    ##########################################################################
    # Identity Module
    ##########################################################################
    def load_identity_domains_main(self):
        try:
            print("Identity Domains...")

            # create identity object
            identity_client = oci.identity.IdentityClient(
                config=self.config,
                signer=self.signer,
                timeout=(self.connection_timeout, self.read_timeout)
            )
            if self.proxy:
                identity_client.base_client.session.proxies = {'https': self.proxy}

            # get tenancy id from the config file
            tenant_id = self.config['tenancy']

            # get all domains
            list_domains = identity_client.list_domains(
                tenant_id,
                lifecycle_state='ACTIVE',
                retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
            ).data

            # oci.identity.models.DomainSummary
            for domain in list_domains:

                # Create Identity Domain Client
                identity_domain_client = oci.identity_domains.IdentityDomainsClient(
                    config=self.config,
                    signer=self.signer,
                    service_endpoint=domain.url,
                    timeout=(self.connection_timeout, self.read_timeout)
                )
                if self.proxy:
                    identity_domain_client.base_client.session.proxies = {'https': self.proxy}

                domain_data = {
                    'id': self.get_value(domain.id),
                    'display_name': self.get_value(domain.display_name),
                    'description': self.get_value(domain.description),
                    'url': self.get_value(domain.url),
                    'home_region_url': self.get_value(domain.home_region_url),
                    'home_region': self.get_value(domain.home_region),
                    'type': self.get_value(domain.type),
                    'license_type': self.get_value(domain.license_type),
                    'is_hidden_on_login': self.get_value(domain.is_hidden_on_login),
                    'time_created': self.get_value(domain.time_created)[0:16],
                    'lifecycle_state': self.get_value(domain.lifecycle_state),
                    'defined_tags': [] if domain.defined_tags is None else domain.defined_tags,
                    'freeform_tags': [] if domain.freeform_tags is None else domain.freeform_tags,
                    'replica_regions': str(','.join(x.region for x in domain.replica_regions)) if domain.replica_regions else "",
                    'users': [],
                    'groups': [],
                    'dynamic_groups': [],
                    'kmsi_setting': [],
                    'identity_providers': [],
                    'authentication_factor_settings': [],
                    'password_policies': []
                }

                ##########################
                # if serial execution
                ##########################
                if self.skip_threads:
                    domain_data['users'] = self.__load_identity_domain_users(identity_domain_client, domain.display_name)
                    domain_data['groups'] = self.__load_identity_domain_groups(identity_domain_client, domain.display_name)
                    domain_data['dynamic_groups'] = self.__load_identity_domain_dynamic_resource_groups(identity_domain_client, domain.display_name)
                    domain_data['kmsi_setting'] = self.__load_identity_domain_kmsi_setting(identity_domain_client, domain.display_name)
                    domain_data['identity_providers'] = self.__load_identity_domain_identity_providers(identity_domain_client, domain.display_name)
                    domain_data['authentication_factor_settings'] = self.__load_identity_domain_authentication_factor_settings(identity_domain_client, domain.display_name)
                    domain_data['password_policies'] = self.__load_identity_domain_password_policies(identity_domain_client, domain.display_name)

                ##########################
                # if parallel execution
                ##########################
                else:
                    with ThreadPoolExecutor(max_workers=8) as executor:
                        future_users = executor.submit(self.__load_identity_domain_users, identity_domain_client, domain.display_name)
                        future_groups = executor.submit(self.__load_identity_domain_groups, identity_domain_client, domain.display_name)
                        future_dynamic_groups = executor.submit(self.__load_identity_domain_dynamic_resource_groups, identity_domain_client, domain.display_name)
                        future_kmsi_setting = executor.submit(self.__load_identity_domain_kmsi_setting, identity_domain_client, domain.display_name)
                        future_identity_providers = executor.submit(self.__load_identity_domain_identity_providers, identity_domain_client, domain.display_name)
                        future_authentication_factor_settings = executor.submit(self.__load_identity_domain_authentication_factor_settings, identity_domain_client, domain.display_name)
                        future_password_policies = executor.submit(self.__load_identity_domain_password_policies, identity_domain_client, domain.display_name)

                        domain_data['users'] = next(as_completed([future_users])).result()
                        domain_data['groups'] = next(as_completed([future_groups])).result()
                        domain_data['dynamic_groups'] = next(as_completed([future_dynamic_groups])).result()
                        domain_data['kmsi_setting'] = next(as_completed([future_kmsi_setting])).result()
                        domain_data['identity_providers'] = next(as_completed([future_identity_providers])).result()
                        domain_data['authentication_factor_settings'] = next(as_completed([future_authentication_factor_settings])).result()
                        domain_data['password_policies'] = next(as_completed([future_password_policies])).result()

                self.data.append(domain_data)

            print("")
            return self.data

        except oci.exceptions.RequestException as e:
            if self.__check_request_error(e):
                return []
            raise
        except oci.exceptions.ServiceError as e:
            if "is not enabled" in str(e):
                print("--> Identity Domains is not enabled.")
                return []
            raise
        except Exception as e:
            self.__print_error("load_identity_domains_main: ", e)
