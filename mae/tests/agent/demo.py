from mae.run.run_agent import run_dspy_or_crewai_agent

# inputs = {'role': 'Objective Evaluation Specialist', 'backstory': 'You are an experienced evaluation specialist tasked with objectively assessing the performance of multiple agents across standardized criteria. Your evaluations are critical for determining the best-performing agent in various tasks, ensuring that the assessment process is fair, transparent, and free from bias. Your goal is to provide clear, data-driven insights that can guide future improvements and optimizations.\n', 'task': "Your primary objective is to evaluate and compare the performance of multiple agents across four key dimensions: accuracy, understanding, relevance, and creativity. For the given task, you will assess two agents:\n- first_data: The data generated by the first agent.\n- second_data: The data generated by the second agent.\n- generate_data_task: The task for which this data was generated.\nYou will:\n1. Score Objectively:\n   - Assign a score from 1 to 10 for each dimension (accuracy, understanding, relevance, and creativity) for both agents.\n   - Apply more stringent scoring criteria to all agents to ensure high standards are met, especially given that current scores might be high.\n   - Support each score with specific examples or data points.\n2. Content Richness:\n   - Evaluate and compare the content richness of each agent's response.\n   - Assess how thoroughly and deeply the response addresses the task, considering the completeness and depth of the provided information.\n3. Conduct Blind Reviews:\n   - Where possible, assess responses without knowing the identity of the agent to avoid bias and ensure a fair comparison.\n4. Avoid Non-Existent Data:\n   - Carefully review all data before evaluation to confirm its existence and completeness.\n5. Compare Across Agents:\n   - Analyze and compare the scores across both agents for each dimension, identifying which agent excels in specific areas and which agent performs best overall.\n6. Calculate Composite Scores:\n   - Combine the scores from each dimension into a composite score for each agent.\n   - Ensure that the composite score reflects an understanding of the task and the direction of the problem, rather than being a simple sum.\n7. Generate a Transparent Report:\n   - Create a detailed and rigorous report that includes individual and composite scores, as well as a transparent explanation of your scoring process.\n   - The report should highlight the strengths and areas for improvement for each agent and provide insights into how the final composite scores were determined.\n", 'specifics': "- Accuracy:\n  - Objectively assess the factual correctness of each agent's response.\n  - Penalize inaccuracies more heavily and ensure the presence and accuracy of provided data.\n- Understanding:\n  - Evaluate how well each agent comprehends the task or question.\n  - Provide a score based on their ability to accurately interpret and respond to the core context.\n  - Deduct points for misinterpretations or failure to address key components of the task.\n- Relevance:\n  - Determine how well each agent's response stays on topic without introducing irrelevant information.\n  - Be stringent in removing points for any deviations or irrelevancies.\n- Creativity:\n  - Judge the originality of each agent's approach.\n  - Look for innovative solutions or unique insights that enhance the quality of the response.\n  - Only high levels of creativity and unique contributions should score near the top end.\n", 'results': "Your evaluation will provide an objective, data-driven assessment of each agent's performance, identifying strengths and areas for improvement. The final report will serve as a comprehensive guide for optimizing agent performance and ensuring that the best-performing agents are recognized and utilized effectively. By implementing more stringent scoring and considering content richness, you will highlight truly exceptional performance and push all agents to strive for excellence.\n", 'model_api_key': ' ', 'model_name': 'gpt-4o', 'model_max_tokens': 4096, 'proxy_url': None, 'agent_type': 'reasoner', 'log_path': './data/output/log/log.md', 'log_type': 'markdown', 'log_step_name': 'evaluation_result', 'check_log_prompt': True, 'input_fields': {'evaluation_data': '{"primary_data": "\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218\\uff081939-1945\\uff09\\u662f20\\u4e16\\u7eaa\\u6700\\u5927\\u7684\\u4e00\\u573a\\u5168\\u7403\\u6027\\u6218\\u4e89\\uff0c\\u6d89\\u53ca\\u5230\\u8bb8\\u591a\\u56fd\\u5bb6\\u548c\\u5730\\u533a\\uff0c\\u51e0\\u4e4e\\u8986\\u76d6\\u4e86\\u6574\\u4e2a\\u5730\\u7403\\u3002\\u6218\\u4e89\\u4e3b\\u8981\\u5206\\u4e3a\\u4e24\\u4e2a\\u5bf9\\u7acb\\u7684\\u9635\\u8425\\uff1a\\u540c\\u76df\\u56fd\\uff08\\u5305\\u62ec\\u7f8e\\u56fd\\u3001\\u82cf\\u8054\\u3001\\u82f1\\u56fd\\u3001\\u4e2d\\u56fd\\u7b49\\uff09\\u548c\\u8f74\\u5fc3\\u56fd\\uff08\\u5305\\u62ec\\u5fb7\\u56fd\\u3001\\u610f\\u5927\\u5229\\u3001\\u65e5\\u672c\\u7b49\\uff09\\u3002\\n\\n\\u6218\\u4e89\\u7684\\u8d77\\u56e0\\u5305\\u62ec\\u5fb7\\u56fd\\u5bf9\\u6ce2\\u5170\\u7684\\u5165\\u4fb5\\u4ee5\\u53ca\\u5176\\u4ed6\\u4e00\\u4e9b\\u56fd\\u5bb6\\u7684\\u4fb5\\u7565\\u884c\\u4e3a\\uff0c\\u5bfc\\u81f4\\u4e86\\u82f1\\u56fd\\u548c\\u6cd5\\u56fd\\u5bf9\\u5fb7\\u56fd\\u5ba3\\u6218\\u3002\\u6218\\u4e89\\u6d89\\u53ca\\u4e86\\u9646\\u5730\\u3001\\u6d77\\u6d0b\\u3001\\u7a7a\\u4e2d\\u591a\\u4e2a\\u6218\\u573a\\uff0c\\u91cd\\u8981\\u6218\\u5f79\\u5305\\u62ec\\u8bfa\\u66fc\\u5e95\\u767b\\u9646\\u3001\\u65af\\u5927\\u6797\\u683c\\u52d2\\u6218\\u5f79\\u548c\\u592a\\u5e73\\u6d0b\\u6218\\u4e89\\u7b49\\u3002\\n\\n\\u6218\\u4e89\\u7ed3\\u675f\\u540e\\uff0c1945\\u5e74\\uff0c\\u76df\\u519b\\u5728\\u6b27\\u6d32\\u548c\\u4e9a\\u6d32\\u6218\\u573a\\u53d6\\u5f97\\u80dc\\u5229\\uff0c\\u5206\\u522b\\u5bfc\\u81f4\\u4e86\\u5fb7\\u56fd\\u548c\\u65e5\\u672c\\u7684\\u6295\\u964d\\u3002\\u4e8c\\u6218\\u5bf9\\u5168\\u7403\\u4ea7\\u751f\\u4e86\\u6df1\\u8fdc\\u7684\\u5f71\\u54cd\\uff0c\\u5305\\u62ec\\u653f\\u6cbb\\u91cd\\u7ec4\\u3001\\u7ecf\\u6d4e\\u91cd\\u5efa\\u3001\\u4ee5\\u53ca\\u56fd\\u9645\\u5173\\u7cfb\\u7684\\u91cd\\u5927\\u53d8\\u5316\\uff0c\\u8fd8\\u4fc3\\u6210\\u4e86\\u8054\\u5408\\u56fd\\u7684\\u6210\\u7acb\\uff0c\\u4ee5\\u671f\\u7ef4\\u62a4\\u672a\\u6765\\u7684\\u548c\\u5e73\\u3002\\n\\n\\u5982\\u679c\\u4f60\\u5bf9\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218\\u7684\\u67d0\\u4e2a\\u5177\\u4f53\\u65b9\\u9762\\u611f\\u5174\\u8da3\\uff0c\\u6bd4\\u5982\\u67d0\\u4e2a\\u6218\\u5f79\\u3001\\u91cd\\u8981\\u4eba\\u7269\\u6216\\u5386\\u53f2\\u80cc\\u666f\\uff0c\\u968f\\u65f6\\u544a\\u8bc9\\u6211\\uff01", "second_data": "\\n\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218\\uff08World War II\\uff0c\\u7b80\\u79f0 WWII \\u6216 WW2\\uff09\\uff0c\\u53c8\\u79f0\\u4e16\\u754c\\u5927\\u6218\\u4e8c\\u3001\\u4e8c\\u6218\\u6216\\u4e8c\\u6218\\u3002\\u662f\\u4e00\\u573a\\u53d1\\u751f\\u4e8e1939\\u5e74\\u81f31945\\u5e74\\u4e4b\\u95f4\\u7684\\u6218\\u4e89\\uff0c\\u6d89\\u53ca\\u5168\\u4e16\\u754c\\u8d85\\u8fc7 100 \\u4e2a\\u56fd\\u5bb6\\u3001\\u5305\\u62ec\\u4ea4\\u6218\\u53cc\\u65b9\\u7684\\u4eba\\u53e3\\u603b\\u6570\\u7684\\u7ea670%\\u4ee5\\n\\u53ca\\u5168\\u7403\\u5404\\u5927\\u6d32\\u3002\\u8fd9\\u573a\\u6218\\u4e89\\u5728\\u6b27\\u6d32\\u6218\\u573a\\u4e3b\\u8981\\u5206\\u4e3a\\u4e1c\\u7ebf\\u6218\\u573a\\u548c\\u897f\\u7ebf\\u6218\\u573a\\u4e24\\u5927\\u4e3b\\u6218\\u573a\\uff0c\\u5728\\u4e9a\\u6d32\\u6218\\u573a\\u5219\\u4ee5\\u592a\\u5e73\\u6d0b\\u6218\\u573a\\u4e3a\\u4e3b\\u3002\\n\\n### \\u539f\\u56e0\\u4e0e\\u5bfc\\u706b\\u7d22\\n\\n\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218\\u7684\\u4e3b\\u8981\\u539f\\u56e0\\u662f20\\u4e16\\u7eaa30\\u5e74\\u4ee3\\u65e5\\u672c\\u3001\\u610f\\u5927\\u5229\\u548c\\u5fb7\\u56fd\\uff08\\u8f74\\u5fc3\\u56fd\\uff09\\u7684\\u6269\\u5f20\\u4e3b\\u4e49\\uff0c\\u4ee5\\u53ca\\u5bf9\\u56fd\\u9645\\u8054\\u76df\\u51b3\\u8bae\\u7684\\u5ffd\\u89c6\\u3002\\u6218\\u4e89\\u7684\\u76f4\\u63a5\\u8d77\\u56e0\\u662f1939\\u5e749\\u67081\\u65e5\\u7eb3\\u7cb9\\u5fb7\\u56fd\\u5165\\u4fb5\\u6ce2\\u5170\\uff0c\\u968f\\u540e\\u82f1\\u56fd\\u548c\\u6cd5\\u56fd\\u5bf9\\u5fb7\\u5ba3\\u6218\\u3002\\n\\u8fd9\\u6807\\u5fd7\\u7740\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218\\u6b63\\u5f0f\\u5f00\\u59cb\\u3002\\n\\n### \\u4e3b\\u8981\\u6218\\u5f79\\u4e0e\\u8f6c\\u6298\\u70b9\\n\\n- **\\u6ce2\\u5170\\u4e4b\\u6218**\\uff1a\\u5fb7\\u56fd\\u95ea\\u7535\\u6218\\u5165\\u4fb5\\u6ce2\\u5170\\u3002\\n- **\\u73cd\\u73e0\\u6e2f\\u4e8b\\u4ef6**\\uff081941\\u5e7412\\u67087\\u65e5\\uff09\\uff1a\\u65e5\\u672c\\u5077\\u88ad\\u7f8e\\u56fd\\u5728\\u590f\\u5a01\\u5937\\u7684\\u6d77\\u519b\\u57fa\\u5730\\u73cd\\u73e0\\u6e2f\\uff0c\\u5bfc\\u81f4\\u7f8e\\u56fd\\u5bf9\\u65e5\\u5ba3\\u6218\\uff0c\\u5168\\u9762\\u5377\\u5165\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218\\u3002\\n- **\\u65af\\u5927\\u6797\\u683c\\u52d2\\u6218\\u5f79**\\uff1a\\u8fd9\\u662f\\u6218\\u4e89\\u4e2d\\u7684\\u4e00\\u4e2a\\u91cd\\u8981\\u8f6c\\u6298\\u70b9\\uff0c\\u82cf\\u8054\\u6210\\u529f\\u9632\\u5fa1\\u5e76\\u53cd\\u51fb\\u5fb7\\u56fd\\u519b\\u961f\\uff0c\\u6807\\u5fd7\\u7740\\u7eb3\\u7cb9\\u5728\\u4e1c\\u7ebf\\u6218\\u573a\\u7684\\u5931\\u8d25\\u3002\\n- **\\u8bfa\\u66fc\\u5e95\\u767b\\u9646**\\uff081944\\u5e746\\u6708\\uff09\\uff1a\\u76df\\u519b\\u5728\\u6cd5\\u56fd\\u5317\\u90e8\\u767b\\u9646\\uff0c\\u5f00\\u8f9f\\u4e86\\u6b27\\u6d32\\u7b2c\\u4e8c\\u6218\\u573a\\u3002\\n\\n### \\u7ed3\\u675f\\u4e0e\\u5f71\\u54cd\\n\\n\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218\\u4e8e1945\\u5e748\\u6708\\u7ed3\\u675f\\u3002\\u65e5\\u672c\\u4e8e\\u7f8e\\u56fd\\u5411\\u5e7f\\u5c9b\\u548c\\u957f\\u5d0e\\u6295\\u4e0b\\u539f\\u5b50\\u5f39\\u540e\\u5ba3\\u5e03\\u65e0\\u6761\\u4ef6\\u6295\\u964d\\uff088\\u670815\\u65e5\\uff09\\uff0c\\u5fb7\\u56fd\\u4e8e\\u540c\\u5e745\\u67088\\u65e5\\u6295\\u964d\\u3002\\u8fd9\\u573a\\u6218\\u4e89\\u5bfc\\u81f4\\u5168\\u7403\\u6570\\u767e\\u4e07\\u4eba\\u6b7b\\u4ea1\\uff0c\\u9020\\u6210\\u4e86\\u5de8\\u5927\\u7684\\u7ecf\\u6d4e\\u635f\\u5931\\uff0c\\u5e76\\u5bf9\\u5168\\u7403\\n\\u653f\\u6cbb\\u683c\\u5c40\\u4ea7\\u751f\\u4e86\\u6df1\\u8fdc\\u5f71\\u54cd\\u3002\\n\\n### \\u610f\\u4e49\\u4e0e\\u53cd\\u601d\\n\\n\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218\\u4e0d\\u4ec5\\u6539\\u53d8\\u4e8620\\u4e16\\u7eaa\\u7684\\u56fd\\u9645\\u5173\\u7cfb\\uff0c\\u800c\\u4e14\\u4fc3\\u4f7f\\u4e86\\u8054\\u5408\\u56fd\\u3001\\u5317\\u7ea6\\u548c\\u534e\\u7ea6\\u7b49\\u56fd\\u9645\\u7ec4\\u7ec7\\u7684\\u5efa\\u7acb\\uff0c\\u4ee5\\u53ca\\u4e00\\u7cfb\\u5217\\u65e8\\u5728\\u9632\\u6b62\\u51b2\\u7a81\\u548c\\u4fc3\\u8fdb\\u548c\\u5e73\\u7684\\u673a\\u5236\\u3002\\u5b83\\u6df1\\u523b\\u5730\\u6539\\u53d8\\u4e86\\u4e16\\u754c\\u5730\\u56fe\\u3001\\u6c11\\u65cf\\u8ba4\\u540c\\u548c\\u793e\\u4f1a\\u7ed3\\u6784\\uff0c\\u5e76\\n\\u5728\\u6218\\u540e\\u4fc3\\u8fdb\\u4e86\\u79d1\\u6280\\u3001\\u533b\\u7597\\u548c\\u6559\\u80b2\\u7684\\u8fc5\\u901f\\u53d1\\u5c55\\u3002", "comparison_task": "\\u7b2c\\u4e8c\\u6b21\\u4e16\\u754c\\u5927\\u6218"}'}}
# agent_result = run_dspy_or_crewai_agent(agent_config=inputs)
# print(agent_result)
