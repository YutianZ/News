import React from 'react';
//import './NewsPanel.css';
import NewsCard from '../NewsCard/NewsCard';
class NewsPanel extends React.Component {
    constructor() {
        super();
        this.state = {news: null};
    }

    componentDidMount() {
        this.loadMoreNews();
    }

    loadMoreNews() {
        //TODO: send real http request;
        const news_url = 'http://' + window.location.hostname + ':3000/news';
        const request= new Request(news_url, {method:'GET'});

        fetch(request)
            .then(res => res.json())
            .then(news => {
                this.setState({news: this.state.news ? this.state.news.concat(news) : news
                })
            })
    }
    renderNews() {
        const news_list = this.state.news.map(news => {
            return(
                //every news has a special digest, use it as key
                <a className='list-group-item' key={news.digest} href='#'>
                    <NewsCard news={news}></NewsCard>
                </a>
            );
        });
        return(
            <div className="container-fluid">
                <div className='list-group'>
                    {news_list}
                </div>
            </div>
        )
    }

    render() {
        if(!this.state.news) {
            return(
                <div id='msg-app-loading'>
                    loading...
                </div>
            );
        } else {
            return(
                <div>
                    {this.renderNews()}
                </div>
            );
        }
    }
}

export default NewsPanel;