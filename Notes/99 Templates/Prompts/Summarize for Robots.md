<Prompt>
Summarize the entire chat conversation into structured XML. 
Wrap the entire output in a <ChatMerge> block so it’s clear this is a new entry 
to be appended, not a replacement. 
Include a timestamp placeholder so merged entries can be distinguished.
No need for additional commentary. Just accept the chat merge as context for this conversation.

Required structure:
<ChatMerge>
  <Entry>
    <Canon>
      <Item></Item>
    </Canon>
    <Decisions>
      <Item></Item>
    </Decisions>
    <OpenLoops>
      <Item></Item>
    </OpenLoops>
    <Discardables>
      <Item></Item>
    </Discardables>
  </Entry>
</ChatMerge>
</Prompt>