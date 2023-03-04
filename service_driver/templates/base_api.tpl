import requests

import os

from service_driver.utils.service_logger import Logger


class BaseApi:
    from http.client import HTTPConnection
    HTTPConnection.debuglevel = 1

    headers = {}
    json_data = None
    base_uri = ''
    base_dir = os.path.join(os.path.dirname(__file__), '..')
    logger = Logger.getLogger("api", base_dir)

    def req(self, method, url, headers=None, **kwargs):
        """
        发送请求
        :param json: json格式参数
        :param params: url携带参数
        :param data: 表单参数
        :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        :param url: URL for the new :class:`Request` object.
            in the query string for the :class:`Request`.
            object to send in the body of the :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
        :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
            to add for the file.
        :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How many seconds to wait for the server to send data
            before giving up, as a float, or a :ref:`(connect timeout, read
            timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
                the server's TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to ``True``.
        :param stream: (optional) if ``False``, the response content will be immediately downloaded.
        :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.

        """
        self.logger.info(f"======请求接口地址：{url}======请求方式：{method}======请求数据{kwargs.__str__()}")
        if headers:
            self.headers.update(headers)
        try:
            resp = requests.request(method=method, url=self.base_uri + url, headers=self.headers,
                                    **kwargs)
            self.logger.info(f'请求结果：{resp.text}')
        except Exception as e:
            self.logger.error("请求接口错误: " + e.__str__())
            raise e
        try:
            json_data: dict = resp.json()
        except:
            json_data = {}
        json_data.update({'status_code': resp.status_code,
                         'text': resp.text,
                         'resp_time': resp.elapsed.total_seconds(),
                         'headers': resp.headers})
        return json_data

    def get_req(self, **kwargs):
        """
        get 请求
        """
        return self.req("get", **kwargs)

    def post_req(self, **kwargs):
        """
        post 请求
        """
        return self.req("post", **kwargs)

    def put_req(self, **kwargs):
        """
        put 请求
        """
        return self.req("put", **kwargs)

    def delete_req(self, **kwargs):
        """
        delete 请求
        """
        return self.req("DELETE", **kwargs)
