"""frontend.main"""

import json

from flask import Flask, request, render_template
from concurrent.futures import ThreadPoolExecutor

from agent_connector import Agent

tools = [
    'exeinfope',
    'pestudio'
]

app = Flask('hhfrontend')
executor = ThreadPoolExecutor(2)

agent_controllers = dict()
with open('agents.json', 'r') as f:
    agents = json.loads(f.read())


@app.route('/')
def index():
    return render_template('index.html', agents=agents)


@app.route('/agent/<agent_name>')
def agent(agent_name):
    # TODO: handle bad agent name request
    agent_data = agents[agent_name]
    agent_controllers[agent_name] = Agent(agent_name, agent_data['ip'], agent_data['port'])
    executor.submit(agent_controllers[agent_name].start)
    return render_template('agent.html', tools=tools, agent_name=agent_name)


@app.route('/run/<agent_name>/<tool_name>')
def run(agent_name, tool_name):
    agent_controllers[agent_name].tool_to_run = tool_name
    print(f'Running {agent_name} {tool_name}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
