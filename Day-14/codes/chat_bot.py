import streamlit as st
import time
from db_Helper import DBHelper
import datetime
import json
st.set_page_config('Agentic Chat UI')
st.subheader('Write a Task to Delegate')
db_helper=DBHelper()
db_helper.select_collection('task')
def dict_to_string(task):
    return ('Title: {title},description: {description},action: {action},contact_name: {contact_name},contact_phone: {contact_phone}').format_map(task)
if 'messages' not in st.session_state:
    st.session_state.messages=[]

# Used loop for showing the previous chats too
for message in st.session_state.messages:
     with st.chat_message(message['role']):
            st.markdown(message['content'])

task_clues = {
    'how to create a task': 'create task: title, description, action(call etc), contact_name, contact_phone',
    'how to view tasks': 'list all tasks',
    'how to update task': 'update task:  title, description, action(call etc), contact_name, contact_phone',
    'how to delete task': 'delete task: title',
}
user_input=st.chat_input('Enter your task here.')
if user_input:
    message={
        'role':'user',
        'content':user_input
    }
    with st.chat_message(message['role']):
        st.markdown(message['content'])
    st.session_state.messages.append(message)
    if user_input in task_clues:
        clue=task_clues[user_input]
        message={
        'role':'assistant',
        'content':clue
        }

        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder=st.empty()
            typing_text=''
            for character in message['content']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.02)
            
    elif 'create task' in user_input:
        data1=user_input.split(':')
        data2=data1[1].split(',')
        task={
            'title':data2[0].strip(),
            'description': data2[1].strip() , 
            'action': data2[2].strip(), 
            'contact_name':data2[3].strip(), 
            'contact_phone':data2[4].strip(),
            'status':'pending',
            'time':datetime.datetime.now( )
        }
        db_helper.save_document(task)
        message={
            'role':'assistant',
            'content':'Task saved successfully'
        }
        with st.chat_message(message['role']):
            typing_placeholder=st.empty()
            typing_text=''
            for character in message['content']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.02)
        
    elif 'list' in user_input:
        document=db_helper.retrieve() 
        
        tasks=''
        for doc in document:
            tasks+=dict_to_string(doc)
            print('Tasks: ', tasks)
        message={
            'role':'assistant',
            'content':tasks
        }
        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder=st.empty()
            typing_text=''
            for character in message['content']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.02)

    elif 'update' in user_input:
        data1=user_input.split(':')
        data2=data1[1].split(',')
        title=data2[0].strip()
        condition={'title':title}
        updated_data={
            'description': data2[1].strip() , 
            'action': data2[2].strip(), 
            'contact_name':data2[3].strip(), 
            'contact_phone':data2[4].strip(),
            'status':'pending',
            'time':datetime.datetime.now( )
        }
        db_helper.update(condition,updated_data)
        message={
            'role':'assistant',
            'content':'Updates Successfully.'
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder=st.empty()
            typing_text=''
            for character in message['content']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.02)
    elif 'delete' in user_input:
        data1=user_input.split(':')
        title=data1[1].strip()
        condition={'title':title}

        deleted_count=db_helper.delete_document(condition)
        if deleted_count and deleted_count>0:
            content='Deleted Successfully.'
        else:
            content='Document was not found.'
        message={
            'role':'assistant',
            'content':content
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder=st.empty()
            typing_text=''
            for character in message['content']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.02)
    else:
        message={
        'role':'assistant',
        'content':'Sorry, request not served.'
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder=st.empty()
            typing_text=''
            for character in message['content']:
                typing_text+=character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.02)