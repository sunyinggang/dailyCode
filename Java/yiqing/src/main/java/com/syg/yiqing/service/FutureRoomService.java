package com.syg.yiqing.service;

import com.syg.yiqing.dao.FutureRoomDao;
import com.syg.yiqing.entity.FutureRoom;
import org.assertj.core.util.Lists;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.stereotype.Service;

import javax.persistence.criteria.CriteriaBuilder;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Predicate;
import javax.persistence.criteria.Root;
import java.util.Date;
import java.text.ParseException;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class FutureRoomService {

    @Autowired
    private FutureRoomDao futureRoomDao;

    public Page<FutureRoom> findAllByCity(PageRequest pageable,String city){
        return futureRoomDao.findAllByCity(pageable,city);
    }
    public Page<FutureRoom> findListLimitTime(PageRequest pageable,String city, Date startTime, Date endTime){
        Page<FutureRoom> list = null;

        if(city != null){
            if(startTime != null && endTime != null){
                list = futureRoomDao.findListLimitCityAndTime(pageable, city, startTime, endTime);
            }else{
                list = futureRoomDao.findAllByCity(pageable, city);
            }
        }else{
            if(startTime != null && endTime != null){
                list = futureRoomDao.findListLimitTime(pageable, startTime, endTime);
            }
        }
        return list;
    }
//    public Page<FutureRoom> findListLimitTimeNoCity(PageRequest pageable,)
}
