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
    "networkcloud cluster update-version",
)
class UpdateVersion(AAZCommand):
    """Update the version of the provided cluster to one of the available supported versions.

    :example: Update cluster version
        az networkcloud cluster update-version --cluster-name "clusterName" --target-cluster-version "2.0" --resource-group "resourceGroupName"
    """

    _aaz_info = {
        "version": "2023-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/clusters/{}/updateversion", "2023-07-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["-n", "--name", "--cluster-name"],
            help="The name of the cluster.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "ClusterUpdateVersionParameters"

        _args_schema = cls._args_schema
        _args_schema.target_cluster_version = AAZStrArg(
            options=["--target-cluster-version"],
            arg_group="ClusterUpdateVersionParameters",
            help="The version to be applied to the cluster during update.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ClustersUpdateVersion(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ClustersUpdateVersion(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [204]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_204,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}/updateVersion",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
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
                    "api-version", "2023-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("targetClusterVersion", AAZStrType, ".target_cluster_version", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

        def on_204(self, session):
            pass

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateVersionHelper._build_schema_operation_status_result_read(cls._schema_on_200_201)

            return cls._schema_on_200_201


class _UpdateVersionHelper:
    """Helper class for UpdateVersion"""

    _schema_error_detail_read = None

    @classmethod
    def _build_schema_error_detail_read(cls, _schema):
        if cls._schema_error_detail_read is not None:
            _schema.additional_info = cls._schema_error_detail_read.additional_info
            _schema.code = cls._schema_error_detail_read.code
            _schema.details = cls._schema_error_detail_read.details
            _schema.message = cls._schema_error_detail_read.message
            _schema.target = cls._schema_error_detail_read.target
            return

        cls._schema_error_detail_read = _schema_error_detail_read = AAZObjectType()

        error_detail_read = _schema_error_detail_read
        error_detail_read.additional_info = AAZListType(
            serialized_name="additionalInfo",
            flags={"read_only": True},
        )
        error_detail_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_detail_read.message = AAZStrType(
            flags={"read_only": True},
        )
        error_detail_read.target = AAZStrType(
            flags={"read_only": True},
        )

        additional_info = _schema_error_detail_read.additional_info
        additional_info.Element = AAZObjectType()

        _element = _schema_error_detail_read.additional_info.Element
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_detail_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_detail_read(details.Element)

        _schema.additional_info = cls._schema_error_detail_read.additional_info
        _schema.code = cls._schema_error_detail_read.code
        _schema.details = cls._schema_error_detail_read.details
        _schema.message = cls._schema_error_detail_read.message
        _schema.target = cls._schema_error_detail_read.target

    _schema_operation_status_result_read = None

    @classmethod
    def _build_schema_operation_status_result_read(cls, _schema):
        if cls._schema_operation_status_result_read is not None:
            _schema.end_time = cls._schema_operation_status_result_read.end_time
            _schema.error = cls._schema_operation_status_result_read.error
            _schema.id = cls._schema_operation_status_result_read.id
            _schema.name = cls._schema_operation_status_result_read.name
            _schema.operations = cls._schema_operation_status_result_read.operations
            _schema.percent_complete = cls._schema_operation_status_result_read.percent_complete
            _schema.resource_id = cls._schema_operation_status_result_read.resource_id
            _schema.start_time = cls._schema_operation_status_result_read.start_time
            _schema.status = cls._schema_operation_status_result_read.status
            return

        cls._schema_operation_status_result_read = _schema_operation_status_result_read = AAZObjectType()

        operation_status_result_read = _schema_operation_status_result_read
        operation_status_result_read.end_time = AAZStrType(
            serialized_name="endTime",
        )
        operation_status_result_read.error = AAZObjectType()
        cls._build_schema_error_detail_read(operation_status_result_read.error)
        operation_status_result_read.id = AAZStrType()
        operation_status_result_read.name = AAZStrType()
        operation_status_result_read.operations = AAZListType()
        operation_status_result_read.percent_complete = AAZFloatType(
            serialized_name="percentComplete",
        )
        operation_status_result_read.resource_id = AAZStrType(
            serialized_name="resourceId",
            flags={"read_only": True},
        )
        operation_status_result_read.start_time = AAZStrType(
            serialized_name="startTime",
        )
        operation_status_result_read.status = AAZStrType(
            flags={"required": True},
        )

        operations = _schema_operation_status_result_read.operations
        operations.Element = AAZObjectType()
        cls._build_schema_operation_status_result_read(operations.Element)

        _schema.end_time = cls._schema_operation_status_result_read.end_time
        _schema.error = cls._schema_operation_status_result_read.error
        _schema.id = cls._schema_operation_status_result_read.id
        _schema.name = cls._schema_operation_status_result_read.name
        _schema.operations = cls._schema_operation_status_result_read.operations
        _schema.percent_complete = cls._schema_operation_status_result_read.percent_complete
        _schema.resource_id = cls._schema_operation_status_result_read.resource_id
        _schema.start_time = cls._schema_operation_status_result_read.start_time
        _schema.status = cls._schema_operation_status_result_read.status


__all__ = ["UpdateVersion"]
