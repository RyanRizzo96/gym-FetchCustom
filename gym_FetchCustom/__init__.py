from gym.envs.registration import register

register(
    id='FetchCustom-v0',
    entry_point='gym_FetchCustom.envs:FetchCustomEnv',
)
