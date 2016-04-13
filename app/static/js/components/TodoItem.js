/**
 * Created by xiaxuan on 16/3/26.
 */
var React = require('react');

var TodoItem = React.createClass({
    handlerUpdate: function(id, status) {
        this.props.updateTodo(id, status);
    },
    handlerDelete: function(id) {
        this.props.deleteTodo(id);
    },
    render: function() {
        var t = this.props.todo;
        var updateBtn;

        if(t.status == 0){
            updateBtn =  <button onClick={this.handlerUpdate.bind(this, t.id, 1)} className="btn btn-primary">Done</button>
        }else{
            updateBtn = <button class="btn-distance"  onClick={this.handlerUpdate.bind(this, t.id, 0)} className="btn btn-primary">Undone</button>
        }
        return (
            <tr>
               <td>{ t.content }</td>
               <td>{ t.status == 0 ? '未完成':'已完成' }</td>
               <td>{ t.time }</td>
               <td>
                   {updateBtn}
                   <button  onClick={this.handlerDelete.bind(this, t.id)} className="btn btn-danger">Delete</button>
               </td>
            </tr>
        );
    }
});

module.exports = TodoItem;