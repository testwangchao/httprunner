# NOTICE: Generated By HttpRunner. DO'NOT EDIT!
# FROM: examples/postman_echo/request_methods/request_with_functions.yml
from httprunner import HttpRunner, TConfig, TStep


class TestCaseRequestWithFunctions(HttpRunner):
    config = TConfig(
        **{
            "name": "request with functions",
            "variables": {"foo1": "session_bar1", "var1": "testsuite_val1"},
            "base_url": "https://postman-echo.com",
            "verify": False,
            "path": "examples/postman_echo/request_methods/demo_testsuite_yml/request_with_functions_test.py",
        }
    )

    teststeps = [
        TStep(
            **{
                "name": "get with params",
                "variables": {
                    "foo1": "bar1",
                    "foo2": "session_bar2",
                    "sum_v": "${sum_two(1, 2)}",
                },
                "request": {
                    "method": "GET",
                    "url": "/get",
                    "params": {"foo1": "$foo1", "foo2": "$foo2", "sum_v": "$sum_v"},
                    "headers": {"User-Agent": "HttpRunner/${get_httprunner_version()}"},
                },
                "extract": {"session_foo2": "body.args.foo2"},
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.args.foo1", "session_bar1"]},
                    {"eq": ["body.args.sum_v", 3]},
                    {"eq": ["body.args.foo2", "session_bar2"]},
                ],
            }
        ),
        TStep(
            **{
                "name": "post raw text",
                "variables": {"foo1": "hello world", "foo3": "$session_foo2"},
                "request": {
                    "method": "POST",
                    "url": "/post",
                    "headers": {
                        "User-Agent": "HttpRunner/${get_httprunner_version()}",
                        "Content-Type": "text/plain",
                    },
                    "data": "This is expected to be sent back as part of response body: $foo1-$foo3.",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {
                        "eq": [
                            "body.data",
                            "This is expected to be sent back as part of response body: session_bar1-session_bar2.",
                        ]
                    },
                ],
            }
        ),
        TStep(
            **{
                "name": "post form data",
                "variables": {"foo1": "bar1", "foo2": "bar2"},
                "request": {
                    "method": "POST",
                    "url": "/post",
                    "headers": {
                        "User-Agent": "HttpRunner/${get_httprunner_version()}",
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                    "data": "foo1=$foo1&foo2=$foo2",
                },
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["body.form.foo1", "session_bar1"]},
                    {"eq": ["body.form.foo2", "bar2"]},
                ],
            }
        ),
    ]


if __name__ == "__main__":
    TestCaseRequestWithFunctions().test_start()
