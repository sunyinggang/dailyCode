package com.syg.yiqing.dao;

import com.syg.yiqing.entity.FutureRoom;
import com.syg.yiqing.entity.TraditionalOffice;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.Date;

public interface TraditionalOfficeDao extends JpaRepository<TraditionalOffice, Integer> {

    @Override
    Page<TraditionalOffice> findAll(Pageable pageable);

    Page<TraditionalOffice> findAllByCity(Pageable pageable,String city);

    @Query("select t from TraditionalOffice t where t.city = :city and t.completion_time >= :openTime")
    Page<TraditionalOffice> findListLimitCityAndTime(Pageable pageable, String city, String openTime);

    @Query("select t from TraditionalOffice t where t.completion_time >= :openTime")
    Page<TraditionalOffice> findListLimitTime(Pageable pageable, String openTime);


}
