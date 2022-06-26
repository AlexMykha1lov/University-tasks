import React, { useContext, useState, useEffect } from 'react';
import {Container, Col, Row, Button} from 'react-bootstrap';
import {observer} from 'mobx-react-lite';
import {Context} from "../index";
import ListsItem from '../components/listsItem';
import CreateListModal from '../components/modals/CreateListModal';
import CreateWordModal from '../components/modals/CreateWordModal';
import { fetchLists } from '../http/listsAPI';

const hobbiesPage = observer(() => {
  const [listModalVisible, setlistModalVisible] = useState(false);
  const [wordModalVisible, setwordModalVisible] = useState(false);
  const {lists} = useContext(Context)

  useEffect(() => {
      fetchLists().then(data => lists.setLists(data))
  }, [])
  return (
    <Container>
      <div className='mt-2 mb-2'><h1>Lists</h1></div>
      <Button className="ms-4" onClick={() => setlistModalVisible(true)}>Add List</Button>
      <Button className="ms-4" onClick={() => setwordModalVisible(true)}>Add word</Button>
      {lists.lists.map(listsItem =>
          <ListsItem key={listsItem.id} listsItem={listsItem}></ListsItem>
        )}
      <CreateListModal show={listModalVisible} onHide={() => setlistModalVisible(false)}></CreateListModal>
      <CreateWordModal show={wordModalVisible} onHide={() => setwordModalVisible(false)}></CreateWordModal>
    
    </Container>
  )
});

export default listsPage;