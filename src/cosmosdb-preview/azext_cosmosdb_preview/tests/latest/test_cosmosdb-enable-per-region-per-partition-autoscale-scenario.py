# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class Cosmosdb_previewEnablePerRegionPerPartitionAutoscaleScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_cosmosdb_sql_enable_per_region_per_partition_autoscale', location='australiaeast')
    def test_cosmosdb_enable_per_region_per_partition_autoscale(self):
        self.kwargs.update({
            'acc': self.create_random_name(prefix='prpp-', length=10),
            'loc': 'australiaeast',
            'tar': '0=1200 1=1200',
            'src': '2'
        })

        # create enablePerRegionPerPartitionAutoscale enabled account
        self.cmd('az cosmosdb create -n {acc} -g {rg} --enable-prpp-autoscale true')
        self.cmd('az cosmosdb show -n {acc} -g {rg}', checks=[
            self.check('enablePerRegionPerPartitionAutoscale', True),
        ])
        print('Created enablePerRegionPerPartitionAutoscale enabled account')

        # disable enablePerRegionPerPartitionAutoscale
        self.cmd('az cosmosdb update -n {acc} -g {rg} --enable-prpp-autoscale false')
        self.cmd('az cosmosdb show -n {acc} -g {rg}', checks=[
            self.check('enablePerRegionPerPartitionAutoscale', False),
        ])
        print('Disabled enablePerRegionPerPartitionAutoscale')

        # enable enablePerRegionPerPartitionAutoscale
        self.cmd('az cosmosdb update -n {acc} -g {rg} --enable-prpp-autoscale true')
        self.cmd('az cosmosdb show -n {acc} -g {rg}', checks=[
            self.check('enablePerRegionPerPartitionAutoscale', True),
        ])
        print('Enabled enablePerRegionPerPartitionAutoscale')

        # delete account
        self.cmd('az cosmosdb delete -n {acc} -g {rg} --yes')
