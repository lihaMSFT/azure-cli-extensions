# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "vmware private-cloud wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.avs/privateclouds/{}", "2023-09-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.private_cloud_name = AAZStrArg(
            options=["-n", "--name", "--private-cloud-name"],
            help="Name of the private cloud",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[-\w\._]+$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PrivateCloudsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class PrivateCloudsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AVS/privateClouds/{privateCloudName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "privateCloudName", self.ctx.args.private_cloud_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200.properties
            properties.availability = AAZObjectType()
            properties.circuit = AAZObjectType()
            _WaitHelper._build_schema_circuit_read(properties.circuit)
            properties.dns_zone_type = AAZStrType(
                serialized_name="dnsZoneType",
            )
            properties.encryption = AAZObjectType()
            properties.endpoints = AAZObjectType()
            properties.extended_network_blocks = AAZListType(
                serialized_name="extendedNetworkBlocks",
            )
            properties.external_cloud_links = AAZListType(
                serialized_name="externalCloudLinks",
                flags={"read_only": True},
            )
            properties.identity_sources = AAZListType(
                serialized_name="identitySources",
            )
            properties.internet = AAZStrType()
            properties.management_cluster = AAZObjectType(
                serialized_name="managementCluster",
                flags={"required": True},
            )
            properties.management_network = AAZStrType(
                serialized_name="managementNetwork",
                flags={"read_only": True},
            )
            properties.network_block = AAZStrType(
                serialized_name="networkBlock",
                flags={"required": True},
            )
            properties.nsx_public_ip_quota_raised = AAZStrType(
                serialized_name="nsxPublicIpQuotaRaised",
            )
            properties.nsxt_certificate_thumbprint = AAZStrType(
                serialized_name="nsxtCertificateThumbprint",
                flags={"read_only": True},
            )
            properties.nsxt_password = AAZStrType(
                serialized_name="nsxtPassword",
                flags={"secret": True},
            )
            properties.provisioning_network = AAZStrType(
                serialized_name="provisioningNetwork",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.secondary_circuit = AAZObjectType(
                serialized_name="secondaryCircuit",
            )
            _WaitHelper._build_schema_circuit_read(properties.secondary_circuit)
            properties.vcenter_certificate_thumbprint = AAZStrType(
                serialized_name="vcenterCertificateThumbprint",
                flags={"read_only": True},
            )
            properties.vcenter_password = AAZStrType(
                serialized_name="vcenterPassword",
                flags={"secret": True},
            )
            properties.virtual_network_id = AAZStrType(
                serialized_name="virtualNetworkId",
            )
            properties.vmotion_network = AAZStrType(
                serialized_name="vmotionNetwork",
                flags={"read_only": True},
            )

            availability = cls._schema_on_200.properties.availability
            availability.secondary_zone = AAZIntType(
                serialized_name="secondaryZone",
            )
            availability.strategy = AAZStrType()
            availability.zone = AAZIntType()

            encryption = cls._schema_on_200.properties.encryption
            encryption.key_vault_properties = AAZObjectType(
                serialized_name="keyVaultProperties",
            )
            encryption.status = AAZStrType()

            key_vault_properties = cls._schema_on_200.properties.encryption.key_vault_properties
            key_vault_properties.auto_detected_key_version = AAZStrType(
                serialized_name="autoDetectedKeyVersion",
                flags={"read_only": True},
            )
            key_vault_properties.key_name = AAZStrType(
                serialized_name="keyName",
            )
            key_vault_properties.key_state = AAZStrType(
                serialized_name="keyState",
            )
            key_vault_properties.key_vault_url = AAZStrType(
                serialized_name="keyVaultUrl",
            )
            key_vault_properties.key_version = AAZStrType(
                serialized_name="keyVersion",
            )
            key_vault_properties.version_type = AAZStrType(
                serialized_name="versionType",
            )

            endpoints = cls._schema_on_200.properties.endpoints
            endpoints.hcx_cloud_manager = AAZStrType(
                serialized_name="hcxCloudManager",
                flags={"read_only": True},
            )
            endpoints.hcx_cloud_manager_ip = AAZStrType(
                serialized_name="hcxCloudManagerIp",
                flags={"read_only": True},
            )
            endpoints.nsxt_manager = AAZStrType(
                serialized_name="nsxtManager",
                flags={"read_only": True},
            )
            endpoints.nsxt_manager_ip = AAZStrType(
                serialized_name="nsxtManagerIp",
                flags={"read_only": True},
            )
            endpoints.vcenter_ip = AAZStrType(
                serialized_name="vcenterIp",
                flags={"read_only": True},
            )
            endpoints.vcsa = AAZStrType(
                flags={"read_only": True},
            )

            extended_network_blocks = cls._schema_on_200.properties.extended_network_blocks
            extended_network_blocks.Element = AAZStrType()

            external_cloud_links = cls._schema_on_200.properties.external_cloud_links
            external_cloud_links.Element = AAZStrType()

            identity_sources = cls._schema_on_200.properties.identity_sources
            identity_sources.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.identity_sources.Element
            _element.alias = AAZStrType()
            _element.base_group_dn = AAZStrType(
                serialized_name="baseGroupDN",
            )
            _element.base_user_dn = AAZStrType(
                serialized_name="baseUserDN",
            )
            _element.domain = AAZStrType()
            _element.name = AAZStrType()
            _element.password = AAZStrType(
                flags={"secret": True},
            )
            _element.primary_server = AAZStrType(
                serialized_name="primaryServer",
            )
            _element.secondary_server = AAZStrType(
                serialized_name="secondaryServer",
            )
            _element.ssl = AAZStrType()
            _element.username = AAZStrType()

            management_cluster = cls._schema_on_200.properties.management_cluster
            management_cluster.cluster_id = AAZIntType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            management_cluster.cluster_size = AAZIntType(
                serialized_name="clusterSize",
            )
            management_cluster.hosts = AAZListType()
            management_cluster.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            management_cluster.vsan_datastore_name = AAZStrType(
                serialized_name="vsanDatastoreName",
            )

            hosts = cls._schema_on_200.properties.management_cluster.hosts
            hosts.Element = AAZStrType()

            sku = cls._schema_on_200.sku
            sku.capacity = AAZIntType()
            sku.family = AAZStrType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.size = AAZStrType()
            sku.tier = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_circuit_read = None

    @classmethod
    def _build_schema_circuit_read(cls, _schema):
        if cls._schema_circuit_read is not None:
            _schema.express_route_id = cls._schema_circuit_read.express_route_id
            _schema.express_route_private_peering_id = cls._schema_circuit_read.express_route_private_peering_id
            _schema.primary_subnet = cls._schema_circuit_read.primary_subnet
            _schema.secondary_subnet = cls._schema_circuit_read.secondary_subnet
            return

        cls._schema_circuit_read = _schema_circuit_read = AAZObjectType()

        circuit_read = _schema_circuit_read
        circuit_read.express_route_id = AAZStrType(
            serialized_name="expressRouteID",
            flags={"read_only": True},
        )
        circuit_read.express_route_private_peering_id = AAZStrType(
            serialized_name="expressRoutePrivatePeeringID",
            flags={"read_only": True},
        )
        circuit_read.primary_subnet = AAZStrType(
            serialized_name="primarySubnet",
            flags={"read_only": True},
        )
        circuit_read.secondary_subnet = AAZStrType(
            serialized_name="secondarySubnet",
            flags={"read_only": True},
        )

        _schema.express_route_id = cls._schema_circuit_read.express_route_id
        _schema.express_route_private_peering_id = cls._schema_circuit_read.express_route_private_peering_id
        _schema.primary_subnet = cls._schema_circuit_read.primary_subnet
        _schema.secondary_subnet = cls._schema_circuit_read.secondary_subnet


__all__ = ["Wait"]
