from infrastructure.config.database import engine, Base

from dependencies import get_hello_world_use_case

Base.metadata.create_all(bind=engine)

use_case = get_hello_world_use_case()
response = use_case.execute()
print(response.message)
