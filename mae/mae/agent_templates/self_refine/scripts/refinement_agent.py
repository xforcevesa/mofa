#!/usr/bin/envs python3
# -*- coding: utf-8 -*-
import json
from dora import DoraStatus
import pyarrow as pa

from mae.kernel.utils.util import load_agent_config
from mae.run.run_agent import run_dspy_agent, run_crewai_agent
from mae.utils.files.dir import get_relative_path


class Operator:
    def on_event(
            self,
            dora_event,
            send_output,
    ) -> DoraStatus:
        if dora_event["type"] == "INPUT":
            if dora_event['id'] == 'feedback_result':
                yaml_file_path = get_relative_path(current_file=__file__, sibling_directory_name='configs',
                                                   target_file_name='feedback_agent.yml')
                inputs = load_agent_config(yaml_file_path)
                result = """
                """
                dora_result = json.loads(dora_event["value"][0].as_py())
                inputs['context'] = dora_result.get('context')
                inputs['input_fields'] = {'suggestion':dora_result.get('suggestion')}

                print(inputs)
                if 'agents' not in inputs.keys():
                    result = run_dspy_agent(agent_config=inputs)
                else:
                    result = run_crewai_agent(crewai_config=inputs)
                if inputs.get('max_iterations',None) is not None:

                    result = {'suggestion':result,'context':result,'local_iterations':dora_result.get('local_iterations', None)}
                else:
                    result = {'suggestion':result,'context':result,}
                print(result)
                send_output("refinement_result", pa.array([json.dumps(result)]),dora_event['metadata'])  # add this line
        return DoraStatus.CONTINUE



