package com.syg.yiqing.service;

import com.syg.yiqing.dao.FutureRoomDao;
import com.syg.yiqing.entity.FutureRoom;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class FutureRoomService {

    @Autowired
    private FutureRoomDao futureRoomDao;

    public Page<FutureRoom> findAllByCity(PageRequest pageable,String city){
        return futureRoomDao.findAllByCity(pageable,city);
    }
}
