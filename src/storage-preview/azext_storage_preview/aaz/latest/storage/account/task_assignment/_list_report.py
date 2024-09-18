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
    "storage account task-assignment list-report",
    is_preview=True,
)
class ListReport(AAZCommand):
    """List the report summary of a single storage task assignment's instances
    """

    _aaz_info = {
        "version": "2023-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.storage/storageaccounts/{}/storagetaskassignments/{}/reports", "2023-05-01"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.account_name = AAZStrArg(
            options=["--account-name"],
            help="The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-z0-9]+$",
                max_length=24,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.storage_task_assignment_name = AAZStrArg(
            options=["-n", "--name", "--storage-task-assignment-name"],
            help="The name of the storage task assignment within the specified resource group. Storage task assignment names must be between 3 and 24 characters in length and use numbers and lower-case letters only.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-z0-9]{3,24}$",
                max_length=24,
                min_length=3,
            ),
        )
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="Optional. When specified, it can be used to query using reporting properties. See [Constructing Filter Strings](https://learn.microsoft.com/en-us/rest/api/storageservices/querying-tables-and-entities#constructing-filter-strings) for details.",
        )
        _args_schema.maxpagesize = AAZIntArg(
            options=["--maxpagesize"],
            help="Optional, specifies the maximum number of storage task assignment instances to be included in the list response.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.StorageTaskAssignmentInstancesReportList(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class StorageTaskAssignmentInstancesReportList(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/storageTaskAssignments/{storageTaskAssignmentName}/reports",
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
                    "accountName", self.ctx.args.account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "storageTaskAssignmentName", self.ctx.args.storage_task_assignment_name,
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
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "$maxpagesize", self.ctx.args.maxpagesize,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-05-01",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"read_only": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.finish_time = AAZStrType(
                serialized_name="finishTime",
                flags={"read_only": True},
            )
            properties.object_failed_count = AAZStrType(
                serialized_name="objectFailedCount",
                flags={"read_only": True},
            )
            properties.objects_operated_on_count = AAZStrType(
                serialized_name="objectsOperatedOnCount",
                flags={"read_only": True},
            )
            properties.objects_succeeded_count = AAZStrType(
                serialized_name="objectsSucceededCount",
                flags={"read_only": True},
            )
            properties.objects_targeted_count = AAZStrType(
                serialized_name="objectsTargetedCount",
                flags={"read_only": True},
            )
            properties.run_result = AAZStrType(
                serialized_name="runResult",
                flags={"read_only": True},
            )
            properties.run_status_enum = AAZStrType(
                serialized_name="runStatusEnum",
                flags={"read_only": True},
            )
            properties.run_status_error = AAZStrType(
                serialized_name="runStatusError",
                flags={"read_only": True},
            )
            properties.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"read_only": True},
            )
            properties.storage_account_id = AAZStrType(
                serialized_name="storageAccountId",
                flags={"read_only": True},
            )
            properties.summary_report_path = AAZStrType(
                serialized_name="summaryReportPath",
                flags={"read_only": True},
            )
            properties.task_assignment_id = AAZStrType(
                serialized_name="taskAssignmentId",
                flags={"read_only": True},
            )
            properties.task_id = AAZStrType(
                serialized_name="taskId",
                flags={"read_only": True},
            )
            properties.task_version = AAZStrType(
                serialized_name="taskVersion",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ListReportHelper:
    """Helper class for ListReport"""


__all__ = ["ListReport"]
