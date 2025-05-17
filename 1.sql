INSERT INTO "users" (id, name, role, api_key, deactivated, balance)
VALUES (
    '00000000-0000-0000-0000-000000000001',  -- фиксированный UUID
    'TestUser',
    'USER',  -- строковое значение перечисления UserRole
    '11111111-1111-1111-1111-111111111111',  -- фиктивный api_key
    false,
    '{"USD": 1000.0, "BTC": 0.5}'  -- JSON с балансом
);