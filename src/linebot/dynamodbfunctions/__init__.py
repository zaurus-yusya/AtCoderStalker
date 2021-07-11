# from . import user_regist
# from . import user_delete
# from . import get_user_id
# from . import is_already_stalking
# from . import get_stalking_list
# from . import regist_stalking_list
# from . import delete_stalking_list
# from . import get_new_user_id
# from . import is_first_time_regist_atcoder_id
# from . import regist_atcoder_info

from dynamodbfunctions.user_regist import user_regist
from dynamodbfunctions.user_delete import user_delete
from dynamodbfunctions.get_user_id import get_user_id
from dynamodbfunctions.is_already_stalking import is_already_stalking
from dynamodbfunctions.get_stalking_list import get_stalking_list
from dynamodbfunctions.regist_stalking_list import regist_stalking_list
from dynamodbfunctions.delete_stalking_list import delete_stalking_list
from dynamodbfunctions.get_new_user_id import get_new_user_id
from dynamodbfunctions.is_first_time_regist_atcoder_id import is_first_time_regist_atcoder_id
from dynamodbfunctions.regist_atcoder_info import regist_atcoder_info