import React, { Component } from 'react';
import './App.css';
import axios from 'axios';
import {Form, FormGroup, Label } from 'reactstrap';
import { Bar } from 'react-chartjs-2';

class MyCharts extends Component {
  constructor(props) {
    super(props);
    this.state = {
      us_states: [],
      us_cities: [],
      stateDataList: [],
      cityDataList: [],
      colorSet: [],
      cityColorSet: []
    }
  }

  componentWillMount() {
    var colorArr = [];
    this.setState({colorSet: this.colorGen(colorArr, 255, 0, 0, 0)});
    var cityColorArr = [];
    this.setState({cityColorSet: this.cityColorGen(cityColorArr, 255, 0, 50, 0)});
  }
  
  componentDidMount() {
    axios.get('http://127.0.0.1:8000/states/')
    .then(res => {
      this.setState({ 
        us_states: res.data
      })
    });
    axios.get('http://127.0.0.1:8000/cities/')
    .then(res => {
      this.setState({ 
        us_cities: res.data
      })
    });
  }
  componentDidUpdate() {
    console.log('charts updated');
  }

  colorGen = (colorArr, red, green, blue, count) => {
    colorArr.push('rgba(' + String(red) + ',' + String(green) + ',' + String(blue) + ',0.95)');
    if(count === 50) {
      return colorArr;
    }
    return this.colorGen(colorArr, red - 5, parseInt(green + (50 - count)/5), blue + 3, count + 1);
  }

  cityColorGen = (colorArr, red, green, blue, count) => {
    colorArr.push('rgba(' + String(red) + ',' + String(green) + ',' + String(blue) + ',0.95)');
    if(count === 50) {
      return colorArr;
    }
    if(count === 0) {
      return this.cityColorGen(colorArr, red - 5, green + 150, blue - 1, count + 1);
    }
    return this.cityColorGen(colorArr, red - 5, green + 2, blue - 1, count + 1);
  }

  render() {
    //total incidents
    const sortedTotalIncidents = this.state.us_states.sort(
      function(a, b){
        return b.total_incidents - a.total_incidents;
      }
    );
    var stateIncidentData = {
        labels: sortedTotalIncidents.map( (us_state) => us_state.name),
        datasets: [{
            label: 'Total of Incidents', 
            data: sortedTotalIncidents.map( (us_state) => us_state.total_incidents),
            backgroundColor: this.state.colorSet
        }]
    }

    //total loss
    const sortedByTotalLoss = this.state.us_states.sort(
      function(a, b) {
        return b.total_killed_n_injured - a.total_killed_n_injured;
      }
    )

    var stateLossData = {
      labels: sortedByTotalLoss.map( (us_state) => us_state.name),
      datasets: [{
          label: 'Total of Injured and Killed', 
          data: sortedByTotalLoss.map( (us_state) => us_state.total_killed_n_injured),
          backgroundColor: this.state.colorSet
      }]
    }

    //incidents by 100k
    const sortedBy100k = this.state.us_states.sort(
      function(a, b) {
        return b.incidents_per_100k - a.incidents_per_100k;
      }
    )

    var state100kData = {
      labels: sortedBy100k.map( (us_state) => us_state.name),
      datasets: [{
          label: 'Total Incidents per 100,000 people', 
          data: sortedBy100k.map( (us_state) => Math.ceil(us_state.incidents_per_100k * 100) / 100),
          backgroundColor: this.state.colorSet
      }]
    }

    //city total incidents
    const citySorted = this.state.us_cities.slice(0, 50).sort(
      function(a, b) {
        return b.total_incidents - a.total_incidents;
      }
    )
    var cityData = {
      labels: citySorted.map( (us_city) => us_city.name),
      datasets: [{
          label: 'Total of Incidents', 
          data: citySorted.map( (us_city) => us_city.total_incidents),
          backgroundColor: this.state.cityColorSet
      }]
    }


    return (
      <div className="App">
        <p className="App-intro">
          <Form>
            <FormGroup>
              <Label for="stateIncidentChart">Total Incidents By States</Label>
              <Bar name="stateIncidentChart" data={stateIncidentData} options={{}}/>
            </FormGroup>
            <FormGroup>
              <Label for="stateLossChart">Total Loss By States</Label>
              <Bar name="stateLossChart" data={stateLossData}/>
            </FormGroup>
            <FormGroup>
              <Label for="state100kChart">Incidents per 100,000 People By States</Label>
              <Bar name="state100kChart" data={state100kData}/>
            </FormGroup>
            <FormGroup>
              <Label for="cityChart">Total Incidents By Cities (Top 50)</Label>
              <Bar name="cityChart" data={cityData}/>
            </FormGroup>

          </Form>
        </p>
      </div>
    );
  }
}

export default MyCharts;