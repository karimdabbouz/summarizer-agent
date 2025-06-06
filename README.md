# Summarizer Agent

The goal is to build an LLM agent that can accept one or n number of input texts and then flexibly rewrite them into a given format, i.e. a blog post, an article, a newsletter etc.

I want this to be as flexible and modular as possible in order to be able to integrate it into different workflows. I am therefore building the agent as an MCP client using PydanticAI that can connect to MCP servers either for receiving input and/or for sending output. Example workflow: Receive a number of weekly newsletters, repurpose them into a single article and create a draft in Wordpress. Or receive a number of newsletters and summarize them into a single one which is then sent to my mail address using a Gmail MCP server (who reads all those newsletters anyway?)

An agent can be seen as a combination of MCP servers for input and/or output and a system prompt. Hence, agents will be created at startup of the webserver and can then be used through their respective endpoints. They will live in memory and can be altered at runtime through the API. This should work for a small number of agents (running MCP servers is another story, but they will most likely be used by multiple agents anyway). Actions in the CLI app correspond to API endpoints I will later build to use different agents remotely. Cool.

- [x] Parse in txt or md file
- [x] Dynamically create API endpoint for agent (combination of system prompt and tools)
- [ ] Add method to parse input into InputText schema
