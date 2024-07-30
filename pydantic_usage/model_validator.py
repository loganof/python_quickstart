"""
@model_validator validate multiple parameters, supporting mode equals "before","after", "wrap"
1. mode=before:class method, recommend user @classmethod below @model_validator
2. mode=after: instance method
@root_validator has been deprecated, and should be replaced with @model_validator.
"""
