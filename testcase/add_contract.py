from api_object.base_api import BaseApi
from jsonpath import jsonpath
from testcase.base_testcase import TestBase


class TestAdd_contract(TestBase):

    def setup_class(self):
        self.api = BaseApi()

    def test_add_contract(self):
        self.logger.info('用例名称：add_contract')
        self.logger.info('测试步骤：/v1/contract/addStep1')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/contract/addStep1",
            "method": "POST",
            'json': {'customer_type': '0', 'customer_id': '1065', 'party_a_contact': '集团管理员',
                     'party_a_contact_number': '13027980550', 'party_b_contact': '', 'party_b_contact_number': '',
                     'status': '', 'collection_cycle': '0', 'content': '', 'contract_name': '123',
                     'end_time': '2023-03-05', 'manage_org_id': '13397', 'oa_pass_type': '1', 'oa_pass_no': '',
                     'oa_pass_link': '', 'party_a': '测试010', 'party_a_id': '497', 'party_a_type': '1',
                     'party_b': '客户01-t', 'party_b_id': '1065', 'party_other': '', 'start_time': '2023-03-04',
                     'notice_limit': ''},
            'headers': {'nonce': '8959', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'Content-Type': 'application/json;charset=UTF-8', 'curtime': '1677885735',
                        'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': '79b546bbce45b848cf688d4bf77150133a1d9edb'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"
        assert str(jsonpath(resp, '$..data')[0]) == "2989"

        self.logger.info('测试步骤：/v1/publicModule/getServiceSelect')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getServiceSelect",
            "method": "GET",
            'params': {'customer_type': '0'},
            'headers': {'nonce': '6803', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'curtime': '1677885773', 'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': '9a986fb474ed63b39f52307c11f07c6e4e600665'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getProduct')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getProduct",
            "method": "GET",
            'params': {'customer_type': '0', 'service_id': '2073'},
            'headers': {'nonce': '7717', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'curtime': '1677885775', 'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': 'b877fe77da7b642352bdad0729d4fb8dbd691ba3'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getAttrValue')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getAttrValue",
            "method": "GET",
            'params': {'attr_id': '1561'},
            'headers': {'nonce': '753', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'curtime': '1677885777', 'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': 'c2251c8722c3663aa0c5062407f7f190ad3921f4'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getUserOrg')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getUserOrg",
            "method": "GET", 'headers': {'nonce': '4492', 'Authorization': '',
                                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                                         'curtime': '1677885781',
                                         'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                                         'checksum': 'bf35d179bda89cc3674ee261212640403ca46c02'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getContractType')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getContractType",
            "method": "GET",
            'params': {'service_ids': '2073'},
            'headers': {'nonce': '2882', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'curtime': '1677885787', 'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': '7c8e95333cc7fc134114bd2bcce205165f6de855'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getNumberUnit')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getNumberUnit",
            "method": "GET",
            'params': {'customer_type': '0'},
            'headers': {'nonce': '7669', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'curtime': '1677885793', 'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': '427983a865c1e7a8f6bd39b3e50b663fa32f07cb'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getDateUnit')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getDateUnit",
            "method": "GET", 'headers': {'nonce': '99', 'Authorization': '',
                                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                                         'curtime': '1677885793',
                                         'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                                         'checksum': 'bceac2bf091cda4898f98604fb83678239f095f7'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getInitStep3')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getInitStep3",
            "method": "GET",
            'params': {'contract_id': '2989'},
            'headers': {'nonce': '4070', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'curtime': '1677885793', 'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': 'd020c82a5b5f5eef2fd9e59b77017d3416a3bc52'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getResourceInfo')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getResourceInfo",
            "method": "GET",
            'params': {'product_id': '1581', 'attr_value_id': '2896', 'org_id': '9580'},
            'headers': {'nonce': '1476', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'curtime': '1677885793', 'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': 'bf5bbc2729011b26d149b8ce6447d16920a20dff'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/contract/addStep3')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/contract/addStep3",
            "method": "POST",
            'json': {'service_price': [
                {'org_id': '9580', 'service_id': '2073', 'product_id': '1581', 'attr_value_id': '2896',
                 'month_unit': '天', 'unit_price': 5000, 'unit': '个', 'month_num': '1', 'product_number': '1',
                 'amount_due': '5000', 'resource_id': '13392', 'tax_rate': '3.00', 'proportion': '10',
                 'billing_way': '0', 'start_time': '2023-03-04', 'end_time': '2023-03-04'}], 'order_list': [
                {'org_id': '9580', 'service_id': '2073', 'product_id': '1581', 'attr_value_id': '2896',
                 'month_unit': '天', 'unit_price': 5000, 'unit': '个', 'month_num': '1', 'product_number': '1',
                 'amount_due': '5000', 'resource_id': '13392', 'tax_rate': '3.00', 'proportion': '10',
                 'billing_way': '0', 'start_time': '2023-03-04', 'end_time': '2023-03-04'}], 'project_id': '0',
                     'contract_type_id': '796', 'contract_id': '2989'},
            'headers': {'nonce': '8128', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'Content-Type': 'application/json;charset=UTF-8', 'curtime': '1677885876',
                        'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': '1c276291be077809151c112933dc4ff3170a7a23'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"

        self.logger.info('测试步骤：/v1/publicModule/getInitStep4')
        req_data = {
            "url": "https://cmsapi-test.ienjoys.com/v1/publicModule/getInitStep4",
            "method": "GET",
            'params': {'contract_id': '2989'},
            'headers': {'nonce': '6650', 'Authorization': '',
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                        'curtime': '1677885877', 'systemauth': '6ERMI89c6d5d0ee050ac1036da4251e79f25c40D12A2',
                        'checksum': '239242197ab85823052329ce598852304010cb28'},
        }

        resp = self.api.req(**req_data)
        # 断言
        assert resp.status_code == 200
        assert resp['headers']['Content-Type'] == "application/json"
        assert str(jsonpath(resp, '$..code')[0]) == "1"
        assert str(jsonpath(resp, '$..message')[0]) == "操作成功"
