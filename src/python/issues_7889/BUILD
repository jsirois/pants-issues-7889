resources(
  name='config',
  sources=['config/prod.config'],
)

python_binary(
  source='main.py',
  dependencies=[
    ':config',
  ],
  compatibility='CPython>=2.7,<3',
)
