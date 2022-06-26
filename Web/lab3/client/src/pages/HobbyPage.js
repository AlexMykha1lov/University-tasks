import React, {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import {Container, Row, Col} from 'react-bootstrap'
import { fetchOneHobby } from '../http/HobbiesAPI';

const hobbyPage = () => {
  const [hobby, setHobby] = useState({words:[]});
  const {id} = useParams(); 

  useEffect(() => {
      fetchOneHobby(id).then(data=>setHobby(data))
  }, [])
  return (
    <Container>
      <h2 className="mt-4">{hobby.name}</h2>
      <Row className="mt-4 text-center border-bottom border-dark">
        <Col md={4}>
          <h4>Term</h4>
        </Col>
        <Col md={8}>
          <h4>Meaning</h4>
        </Col>
      </Row>
      {hobby.words.map(word => 
            <Row key={word.id} className="mt-4 text-center border-bottom border-dark">
            <Col md={4}>
              <p>{word.text}</p>
            </Col>
            <Col md={8}>
              <p>{word.extra}</p>
            </Col>
          </Row>
        )}
    </Container>
  )
}

export default hobbyPage;