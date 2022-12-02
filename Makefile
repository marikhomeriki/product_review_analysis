# directive_name:
# <tab>some command with all its arguments
# <tab>@this command will not print out before being executed
# <tab>-the command after this one will run no matter what
# <tab>-@the markers can be combined


test_gcp_setup:
	@TEST_ENV=development pytest \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_setup_key_env \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_setup_key_path \
	tests/setup/test_gcp_setup.py::TestGcpSetup::test_code_get_project
