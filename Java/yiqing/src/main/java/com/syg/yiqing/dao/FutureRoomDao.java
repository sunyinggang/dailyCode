package com.syg.yiqing.dao;

import com.syg.yiqing.entity.FutureRoom;
import com.syg.yiqing.entity.TraditionalOffice;
import org.springframework.data.domain.Example;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.Date;
import java.time.LocalDateTime;

public interface FutureRoomDao extends JpaRepository<FutureRoom, Integer> {

    @Override
    Page<FutureRoom> findAll(Pageable pageable);

    @Override
    <S extends FutureRoom> Page<S> findAll(Example<S> example, Pageable pageable);

    Page<FutureRoom> findAllByCity(Pageable pageable, String city);

    @Query("select f from FutureRoom f where f.city = :city and f.opening_date >= :startTime and f.opening_date <= :endTime")
    Page<FutureRoom> findListLimitCityAndTime(Pageable pageable,String city, Date startTime, Date endTime);

    @Query("select f from FutureRoom f where f.opening_date >= :startTime and f.opening_date <= :endTime")
    Page<FutureRoom> findListLimitTime(Pageable pageable, Date startTime, Date endTime);
}
