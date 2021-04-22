from test_register import *

from test_login import run_test_valid_login

# register fails
run_test_INvalid_register_admin(1)
run_test_INvalid_register_tenant(1)

# register admin accounts
run_test_valid_register_admin(5)

# register tenant accounts
run_test_valid_register_tenant(5)

# login success
run_test_valid_login(10)
