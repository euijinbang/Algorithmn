from typing import List, Text


class NoAgentFoundException(Exception):
    print("NoAgentFound")


class Agent(object):

    def __init__(self, name, skills, load):
        # 에이전트 이름
        self.name = name
        # 에이전트의 스킬 리스트
        self.skills = skills
        # 현재 할당된 티켓의 수
        self.load = load

    # 인스턴스 메소드
    def get_name(self):
        return self.name

    def get_skills(self):
        return self.skills

    def get_load(self):
        return self.load

    def __str__(self):
        return "<Agent: {}>".format(self._name)


class Ticket(object):

    def __init__(self, id, restrictions):
        # 티켓 아이디
        self.id = id
        # 이 티켓을 처리하기 위해 필요한 스킬
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        pass

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        pass


# 정책 1. 에이전트 객체를 반환, 할당된 티켓의 수가 가장 적은 에이전트를 반환
class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if len(agents) != 0:
            loads = []
            for agent in agents:
                load = agent.get_load()
                loads.append(load)

            least = min(loads)
            l_agent = agents[loads.index(least)]
        else:
            raise NoAgentFoundException()

        return l_agent


# 정책 2. 스킬의 수가 가장 적은 에이전트를 반환
class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        if len(agents) != 0:
            skills = []
            for agent in agents:
                skill = agent.get_skills()
                skills.append(skill)

            least = min(skills)
            l_agent = agents[skills.index(least)]
        else:
            raise NoAgentFoundException()

        return l_agent


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = LeastLoadedAgent()
least_loaded_policy.find(ticket, [agent1, agent2])

least_flexible_policy = LeastFlexibleAgent()
least_flexible_policy.find(ticket, [agent1, agent2])
