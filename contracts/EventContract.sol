// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EventContract {
    struct Event {
        uint id;
        address creator;
        string name;
        string description;
        uint timestamp;
    }

    uint public eventCount = 0;
    mapping(uint => Event) public events;

    function createEvent(string memory _name, string memory _description) public {
        eventCount++;
        events[eventCount] = Event(eventCount, msg.sender, _name, _description, block.timestamp);
    }

    function getEvent(uint _id) public view returns (Event memory) {
        return events[_id];
    }
}
