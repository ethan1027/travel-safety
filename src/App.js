import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import {Button, Form, FormGroup, Label, Input, Jumbotron } from 'reactstrap';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      us_states: [],
      us_cities: [],
      stateName: 'Illinois',
      stateRank: 1,
      stateIncidents: 17556,
      stateIncidents100k: 136.52,
      stateTotalLoss: 16923,
      cityName: 'Chicago, Illinois',
      cityRank: 1,
      cityIncidents: 10814,
      stateList: [],
      cityList: []
    }
  }
  componentDidMount() {
    var path = 'https://travel-safety.herokuapp.com/'
    if(window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
      path = 'http://127.0.0.1:8000/'
    }
    console.log(path)
    axios.get(path + 'states/')
    .then(res => {
      this.setState({ 
        us_states: res.data,
        stateList: res.data.map( (us_state) => us_state.name).sort()
      })
    });
    axios.get(path + 'cities/')
    .then(res => {
      this.setState({ 
        us_cities: res.data,
        cityList : res.data.map( (us_city) => us_city.name).sort() 
      })
    });
  }
  componentDidUpdate() {
    console.log('search updated');
  }

  stateSearch = () => {
    var searchValue = document.getElementById("stateSelect").value;
    this.setState({stateName: String(searchValue)});
    var foundObject = this.state.us_states.find(function(element) {
      return element.name == searchValue;
    })
    this.setState({ 
      stateRank: foundObject.rank, 
      stateIncidents: foundObject.total_incidents,
      stateIncidents100k: Math.ceil(foundObject.incidents_per_100k * 100) / 100,
      stateTotalLoss: foundObject.total_killed_n_injured})
  }

  citySearch = () => {
    var searchValue = document.getElementById("citySelect").value;
    this.setState({cityName: String(searchValue)});
    var foundObject = this.state.us_cities.find(function(element) {
      return element.name === searchValue;
    })
    this.setState({cityRank: foundObject.rank,
      cityIncidents: foundObject.total_incidents})
  }

  render() {
    var state_names = this.state.stateList.map( us_state => <option value={us_state}>{us_state}</option>);
    var city_names = this.state.cityList.map( us_city => <option value={us_city}>{us_city}</option>);
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Django-React Project: Travel Safety</h1>
        </header>
        <p className="App-intro">
          <Form>
            <FormGroup>
              <Label for="stateSelect">Choose a State</Label>
              <Input type="select" id="stateSelect" name="stateSelect">
                {state_names}
              </Input>
              <Button color="info" onClick={this.stateSearch}>Submit State</Button>
            </FormGroup>
            <FormGroup>
              <Label for="citySelect">Choose a City/County</Label>
              <Input type="select" id="citySelect" name="citySelect">
                {city_names}
              </Input>
              <Button color="info" onClick={this.citySearch}>Submit City/County</Button>
            </FormGroup>
            <FormGroup>
              <Jumbotron>
                <h2 className="display-4">{this.state.stateName}</h2>
                <p className="lead">is the top {this.state.stateRank} dangerous state in the U.S.</p>
                <p className="lead">has a total of {this.state.stateIncidents} gun-shot incidents from 2014 to 2018.</p>
                <p className="lead">has {this.state.stateIncidents100k} gun-shot incidents per 100,000 people from 2014 to 2018.</p>
                <p className="lead">{this.state.stateTotalLoss} people were killed and injured.</p>
                
                <hr className="my-2" />
                <h2 className="display-4">{this.state.cityName}</h2>
                <p className="lead">is the top {this.state.cityRank} dangerous city/county out of around 17,000 municipalities in the U.S.</p>
                <p className="lead">has a total of {this.state.cityIncidents} gun-shot incidents from 2014 to 2018.</p>
                
              </Jumbotron>
            </FormGroup>
          </Form>
        </p>
      </div>
    );
  }
}

export default App;
